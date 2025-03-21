import unittest
import sys
import os
import time

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestPower4(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_power_4(self):
        time.sleep(1)  # 1 second delay
        self.assertEqual(self.calc.power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
