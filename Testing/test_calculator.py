import unittest

from calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def test_init_calculator(self):
        calculator = Calculator(727)
        self.assertEqual(calculator.current_value, 727)
        self.assertEqual(calculator.results_history, [])

    def test_add(self):
        calculator = Calculator(10)
        calculator.add(273)
        self.assertEqual(calculator.current_value, 283)
        self.assertEqual(calculator.results_history, [10])

    def test_subtract(self):
        calculator = Calculator(11)
        calculator.subtract(-2)
        self.assertEqual(calculator.current_value, 13)
        self.assertEqual(calculator.results_history, [11])

    def test_multiplication(self):
        calculator = Calculator(12)
        calculator.multiply(12)
        self.assertEqual(calculator.current_value, 144)
        self.assertEqual(calculator.results_history, [12])

    def test_division(self):
        calculator = Calculator(12)
        result = calculator.divide(12)
        self.assertEqual(calculator.current_value, 1)
        self.assertEqual(calculator.results_history, [12])
        self.assertTrue(result)

    def test_undo(self):
        calculator = Calculator(100)
        calculator.add(10)
        self.assertEqual(calculator.current_value, 110)
        self.assertEqual(calculator.results_history, [100])
        calculator.undo()
        self.assertEqual(calculator.current_value, 100)
        self.assertEqual(calculator.results_history, [])

    def test_undo_empty_history(self):
        calculator = Calculator(100)
        self.assertEqual(calculator.current_value, 100)
        self.assertEqual(calculator.results_history, [])
        calculator.undo()
        self.assertEqual(calculator.current_value, 0)
        self.assertEqual(calculator.results_history, [])

    def test_zero_division(self):
        calculator = Calculator(999)
        result = calculator.divide(0)
        self.assertEqual(calculator.current_value, 999)
        self.assertEqual(calculator.results_history, [])
        self.assertFalse(result)