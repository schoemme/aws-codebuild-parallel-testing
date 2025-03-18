import os

# Operations to test
operations = [
    ('add', 'a + b', '3, 4', '7'),
    ('subtract', 'a - b', '10, 4', '6'),
    ('multiply', 'a * b', '3, 4', '12'),
    ('divide', 'a / b', '12, 4', '3'),
    ('power', 'a ** b', '2, 3', '8'),
    ('modulo', 'a % b', '10, 3', '1')
]

# Template for test files
test_template = '''import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator

class Test{operation_cap}{test_num}(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_{operation}_{test_num}(self):
        self.assertEqual(self.calc.{operation}({test_args}), {test_result})

if __name__ == '__main__':
    unittest.main()
'''

# Create test files
for op_idx, (operation, _, args, result) in enumerate(operations):
    operation_cap = operation.capitalize()
    
    # Create more files for each operation
    for i in range(1, 51):  # 50 files per operation = 300 files total
        test_num = i + (op_idx * 50)
        
        # Create test file
        filename = f"tests/test_{operation}_{i:03d}.py"
        with open(filename, 'w') as f:
            f.write(test_template.format(
                operation_cap=operation_cap,
                operation=operation,
                test_num=i,
                test_args=args,
                test_result=result
            ))

print(f"Generated {len(operations) * 50} test files in the tests directory.")
