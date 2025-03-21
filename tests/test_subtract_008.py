import unittest
import sys
import os
import time

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestSubtract8(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_subtract_8(self):
        time.sleep(1)  # 1 second delay
        self.assertEqual(self.calc.subtract(10, 4), 6)

if __name__ == '__main__':
    unittest.main()
