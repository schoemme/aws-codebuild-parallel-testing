import unittest
import sys
import os
import time

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestModulo3(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_modulo_3(self):
        time.sleep(1)  # 1 second delay
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()
