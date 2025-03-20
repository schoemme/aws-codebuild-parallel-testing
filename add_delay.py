#!/usr/bin/env python3
import os
import re

def add_sleep_to_test_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Check if time is already imported
    if 'import time' not in content:
        # Add import time statement after the last import
        content = re.sub(r'(import .*?\n)(?!import)', r'\1import time\n\n', content, count=1)
    
    # Find all test methods and add sleep
    test_pattern = r'(    def test_\w+\(self\):\n)'
    if re.search(test_pattern, content):
        modified_content = re.sub(test_pattern, r'\1        time.sleep(1)  # 1 second delay\n', content)
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)
        return True
    return False

def process_test_files(directory):
    modified_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                file_path = os.path.join(root, file)
                if add_sleep_to_test_file(file_path):
                    modified_count += 1
                    print(f"Modified: {file_path}")
    
    print(f"\nAdded 1-minute delay to {modified_count} test files.")

if __name__ == "__main__":
    tests_dir = "./tests"
    process_test_files(tests_dir)
