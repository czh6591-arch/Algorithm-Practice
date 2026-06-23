import subprocess
import tempfile
import os
import json

def execute_python_code(code, test_cases):
    results = []
    errors = []
    
    for i, test_case in enumerate(test_cases):
        input_data = test_case.get('input', '')
        expected_output = test_case.get('output', '')
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            f.flush()
            
            input_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
            input_file.write(input_data)
            input_file.flush()
            
            try:
                result = subprocess.run(
                    ['python', f.name],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                if result.returncode != 0:
                    errors.append(f"测试用例 {i+1} 执行错误: {result.stderr}")
                    results.append({
                        'passed': False,
                        'error': result.stderr,
                        'test_case': i+1
                    })
                else:
                    actual_output = result.stdout.strip()
                    if actual_output == expected_output.strip():
                        results.append({
                            'passed': True,
                            'test_case': i+1
                        })
                    else:
                        results.append({
                            'passed': False,
                            'expected': expected_output.strip(),
                            'actual': actual_output,
                            'test_case': i+1
                        })
            except subprocess.TimeoutExpired:
                errors.append(f"测试用例 {i+1} 超时")
                results.append({
                    'passed': False,
                    'error': '超时',
                    'test_case': i+1
                })
            finally:
                os.unlink(f.name)
                os.unlink(input_file.name)
    
    return results, errors

def analyze_complexity(code):
    time_complexity = "O(n)"
    space_complexity = "O(1)"
    
    if 'for' in code and 'for' in code[code.find('for')+1:]:
        if 'for' in code[code.find('for')+1:][code[code.find('for')+1:].find('for')+1:]:
            time_complexity = "O(n^3)"
        else:
            time_complexity = "O(n^2)"
    
    if 'append' in code or 'list' in code:
        if 'for' in code:
            space_complexity = "O(n)"
    
    return time_complexity, space_complexity

def compare_complexity(actual, expected):
    complexity_order = {'O(1)': 1, 'O(log n)': 2, 'O(n)': 3, 'O(n log n)': 4, 'O(n^2)': 5, 'O(n^3)': 6, 'O(2^n)': 7}
    
    actual_level = complexity_order.get(actual, 0)
    expected_level = complexity_order.get(expected, 0)
    
    return actual_level <= expected_level