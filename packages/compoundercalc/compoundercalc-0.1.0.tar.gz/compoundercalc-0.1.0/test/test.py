import unittest
from compoundercalc.compounder import CompoundInterestCalculator

class TestCompoundInterestCalculator(unittest.TestCase):

    def test_final_amount(self):
        calc = CompoundInterestCalculator(1000, 150, 12, 0.08)
        result = calc.final_amount(10)
        expected = 29661.55  # Este valor debe ser recalculado para asegurarse de que sea correcto.
        self.assertAlmostEqual(result, expected, places=2)

    def test_time_goal(self):
        calc = CompoundInterestCalculator(1000, 150, 12, 0.08)
        years, months, days = calc.time_goal(100000)
        self.assertTrue(years > 0 and months >= 0 and days >= 0)

    def test_calc_recurring_deposit(self):
        calc = CompoundInterestCalculator(1000, 150, 12, 0.08)
        required_deposit = calc.calc_recurring_deposit(100000, 10)
        self.assertTrue(required_deposit > 0)

    def test_calc_interest_rate(self):
        calc = CompoundInterestCalculator(1000, 150, 12, 0.08)
        required_rate = calc.calc_interest_rate(100000, 10)
        self.assertTrue(required_rate > 0)

if __name__ == '__main__':
    unittest.main()
