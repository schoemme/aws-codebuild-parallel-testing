import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestDivide48(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_divide_48(self):
        self.assertEqual(self.calc.divide(12, 4), 3)

if __name__ == '__main__':
    unittest.main()
