Compound Interest Calculator
============================

This package provides a ``CompoundInterestCalculator`` class for
calculating compound interest for various financial scenarios.

Features
--------

-  Calculate the total amount with compound interest over a period of
   time.
-  Determine the time needed to reach a target amount with compound
   interest.
-  Calculate the required recurring deposit to reach a target amount.
-  Calculate the required interest rate to reach a target amount.

Installation
------------

You can install the package using pip:

.. code:: bash

   pip install compoundercalc

Usage
-----

Importing the Calculator
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from compoundercalc.compounder import CompoundInterestCalculator

Creating an Instance
~~~~~~~~~~~~~~~~~~~~

.. code:: python

   calc = CompoundInterestCalculator(initial_deposit=1000, recurring_deposit=150, num_recurring_per_year=12, interest_rate=0.08)

Calculating the Final Amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   result = calc.final_amount(time_years=10)
   print(f"The final amount is: {result:.2f}")

Determining the Time to Reach a Target Amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   years, months, days = calc.time_goal(target_amount=100000)
   print(f"Time needed to reach the goal: {years} years, {months} months, and {days} days")

Calculating the Required Recurring Deposit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   required_deposit = calc.calc_recurring_deposit(target_amount=100000, total_years=10)
   print(f"The required recurring deposit is: {required_deposit:.2f}")

Calculating the Required Interest Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   try:
       required_rate = calc.calc_interest_rate(target_amount=100000, total_years=10)
       print(f"The required annual interest rate is: {required_rate:.4f}")
   except ValueError as e:
       print(e)

Running Tests
-------------

To run the tests, use the following command:

.. code:: bash

   python -m unittest discover -s test

License
-------

This project is licensed under GNU License. See the
`LICENSE <LICENSE>`__ file for details.

Contributing
------------

Contributions are welcome! Please feel free to submit a Pull Request.
