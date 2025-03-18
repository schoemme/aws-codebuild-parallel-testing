import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class TestAdd17(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_17(self):
        self.assertEqual(self.calc.add(3, 4), 7)

if __name__ == '__main__':
    unittest.main()
