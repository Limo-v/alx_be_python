import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)


    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(8, 3), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiply(self):
        """Test the multipy method."""
        self.assertEqual(self.calc.multiply(8, 3), 24)
        self.assertEqual(self.calc.multiply(-3, 3), -9)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        self.assertEqual(self.calc.divide(4, 0), None)

