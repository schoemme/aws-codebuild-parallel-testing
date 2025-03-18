import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestPower3(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_power_3(self):
        self.assertEqual(self.calc.power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
