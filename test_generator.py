import os
import time

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
        time.sleep(1)  # 1 second delay
        self.assertEqual(self.calc.{operation}({test_args}), {test_result})

if __name__ == '__main__':
    unittest.main()
'''

file_per_operations = 300

# Create tests directory if it doesn't exist
tests_dir = "tests"
if not os.path.exists(tests_dir):
    os.makedirs(tests_dir)
    print(f"Created directory: {tests_dir}")

# Create test files
for op_idx, (operation, _, args, result) in enumerate(operations):
    operation_cap = operation.capitalize()
    
    # Create more files for each operation
    for i in range(1, file_per_operations + 1):  # file_per_operations files per operation = 4 * file_per_operations files total
        test_num = i + (op_idx * file_per_operations)
        
        # Create test file
        filename = f"{tests_dir}/test_{operation}_{i:03d}.py"
        with open(filename, 'w') as f:
            f.write(test_template.format(
                operation_cap=operation_cap,
                operation=operation,
                test_num=i,
                test_args=args,
                test_result=result
            ))

print(f"Generated {len(operations) * file_per_operations} test files in the tests directory.")
