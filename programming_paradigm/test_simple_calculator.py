import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        result = SimpleCalculator.add(self, 5, 2)
        self.assertEqual(result, 7)
    
    def test_subtract(self):
        result = SimpleCalculator.subtract(self, 5, 2)
        self.assertEqual(result, 3)
    
    def test_multiply(self):
        result = SimpleCalculator.multiply(self, 5, 2)
        self.assertEqual(result, 10)
    
    def test_divide(self):
        result = SimpleCalculator.divide(self, 5, 2)
        self.assertEqual(result, 2.5)

if __name__ == "__main__":
  unittest.main()