#compounder-calc.py

"""
This module contains the CompoundInterestCalculator class.
"""

class CompoundInterestCalculator:
    """
    A class used to calculate compound interest for various financial scenarios.
    """
    def __init__(self, initial_deposit, recurring_deposit,
                 num_recurring_per_year, interest_rate,
                 total_years=None):
        """
        Initializes the calculator with the given parameters.

        Parameters:
        initial_deposit (float): The initial amount invested.
        recurring_deposit (float): The amount of each recurring deposit.
        num_recurring_per_year (int): The number of recurring deposits per year.
        interest_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        total_years (int, optional): The total number of years. Default is None.
        """
        self.initial_deposit = initial_deposit
        self.recurring_deposit = recurring_deposit
        self.num_recurring_per_year = num_recurring_per_year
        self.interest_rate = interest_rate
        self.total_years = total_years

    def final_amount(self, time_years):
        """
        Calculates the total amount with compound interest.

        Parameters:
        time_years (int): The time in years.

        Returns:
        float: The total amount at the end of the period.
        """
        periods = self.num_recurring_per_year * time_years
        periodic_rate = self.interest_rate / self.num_recurring_per_year

        future_value_initial = self.initial_deposit * (1 + periodic_rate) ** periods
        future_value_recurring = self.recurring_deposit * (
            ((1 + periodic_rate) ** periods - 1) / periodic_rate
        )

        total_amount = future_value_initial + future_value_recurring
        return round(total_amount,2)

    def time_goal(self, target_amount):
        """
        Calculates the time needed to reach a target amount with compound interest.

        Parameters:
        target_amount (float): The desired final amount.

        Returns:
        (int, int, int): The time needed in years, months, and days.
        """
        current_amount = self.initial_deposit
        time_years = 0

        while current_amount < target_amount:
            time_years += 1 / self.num_recurring_per_year
            current_amount = current_amount * (1 + self.interest_rate / self.num_recurring_per_year)
            current_amount += self.recurring_deposit

        # Convert fractional years to years, months, and days
        total_days = time_years * 365
        years, remainder = divmod(total_days, 365)
        months, days = divmod(remainder, 30)

        return int(years), int(months), int(days)

    def calc_recurring_deposit(self, target_amount, total_years):
        """
        Calculates the required recurring deposit to reach a target amount with compound interest.

        Parameters:
        target_amount (float): The desired final amount.
        total_years (int): The total number of years.

        Returns:
        float: The required recurring deposit amount.
        """
        periods = self.num_recurring_per_year * total_years
        periodic_rate = self.interest_rate / self.num_recurring_per_year

        # Calculate future value of the initial deposit
        future_value_initial = self.initial_deposit * (1 + periodic_rate) ** periods

        # Calculate the future value factor for recurring deposits
        future_value_factor = ((1 + periodic_rate) ** periods - 1) / periodic_rate

        # Calculate the required recurring deposit
        required_recurring_deposit = (target_amount - future_value_initial) / future_value_factor

        return required_recurring_deposit

    def calc_interest_rate(self, target_amount, total_years, tolerance=1e-6, max_iterations=1000):
        """
        Calculates the required interest rate to reach a target amount with compound interest.

        Parameters:
        target_amount (float): The desired final amount.
        total_years (int): The total number of years.
        tolerance (float): The tolerance level for convergence of the interest rate.
        max_iterations (int): The maximum number of iterations for the rate calculation.

        Returns:
        float: The required annual interest rate as a decimal rounded to four decimal places 
        (e.g., 0.0500 for 5%).

        Raises:
        ValueError: If the interest rate calculation does not converge within the specified 
        number of iterations.
        """
        def calculate_future_value(rate):
            periods = self.num_recurring_per_year * total_years
            periodic_rate = rate / self.num_recurring_per_year
            future_value_initial = self.initial_deposit * (1 + periodic_rate) ** periods
            future_value_recurring = self.recurring_deposit * (((1 + periodic_rate) ** periods - 1) / periodic_rate)
            return future_value_initial + future_value_recurring

        low_rate = 0.0
        high_rate = 1.0

        for _ in range(max_iterations):
            mid_rate = (low_rate + high_rate) / 2
            future_value = calculate_future_value(mid_rate)
            if abs(future_value - target_amount) < tolerance:
                return round(mid_rate, 4)
            elif future_value < target_amount:
                low_rate = mid_rate
            else:
                high_rate = mid_rate

        raise ValueError(
            f"Interest rate calculation did not converge after {max_iterations} iterations. "
            f"Try increasing the number of iterations or adjusting the rate range. "
            f"Current range: [{low_rate:.6f}, {high_rate:.6f}]"
        )
