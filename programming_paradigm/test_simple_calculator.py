#test_simple_calculator
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()

    #Addition Tests
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    #Subtraction Tests
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 7), -4)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_subtraction_same_numbers(self):
        self.assertEqual(self.calc.subtract(8, 8), 0)

    #Multiplication Tests
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    #Division Tests
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_floating_point(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_negative_result(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
