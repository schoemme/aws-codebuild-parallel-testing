import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestSubtract29(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_subtract_29(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

if __name__ == '__main__':
    unittest.main()
