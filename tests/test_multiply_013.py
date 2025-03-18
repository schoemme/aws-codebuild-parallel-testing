import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestMultiply13(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_multiply_13(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

if __name__ == '__main__':
    unittest.main()
