# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance for testing."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Normal case
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive
        self.assertEqual(self.calc.add(-3, -7), -10)  # Both negative
        self.assertEqual(self.calc.add(0, 0), 0)  # Both zero
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)  # Floating-point

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)  # Normal case
        self.assertEqual(self.calc.subtract(5, 10), -5)  # Result negative
        self.assertEqual(self.calc.subtract(-5, -5), 0)  # Both negative
        self.assertEqual(self.calc.subtract(0, 5), -5)  # From zero
        self.assertEqual(self.calc.subtract(3.5, 1.5), 2.0)  # Floating-point

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)  # Normal case
        self.assertEqual(self.calc.multiply(-4, 5), -20)  # Negative and positive
        self.assertEqual(self.calc.multiply(-4, -5), 20)  # Both negative
        self.assertEqual(self.calc.multiply(0, 100), 0)  # By zero
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)  # Floating-point

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # Normal case
        self.assertEqual(self.calc.divide(-10, 2), -5)  # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5)  # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5)  # Both negative
        self.assertEqual(self.calc.divide(7, 2), 3.5)  # Floating-point result
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero numerator
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero

if __name__ == "__main__":
    unittest.main()
