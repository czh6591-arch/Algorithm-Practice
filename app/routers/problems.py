from fastapi import APIRouter, HTTPException, Depends
import json
from app.database import get_db
from app.security import get_current_user
from app.code_executor import execute_python_code, analyze_complexity, compare_complexity

router = APIRouter()

@router.get("/problems")
def get_problems(difficulty: str = None):
    db = get_db()
    if difficulty:
        problems = db.execute('SELECT * FROM problems WHERE difficulty = ?', (difficulty,)).fetchall()
    else:
        problems = db.execute('SELECT * FROM problems').fetchall()
    
    result = []
    for problem in problems:
        pass_rate = 0
        if problem['attempt_count'] > 0:
            pass_rate = (problem['pass_count'] / problem['attempt_count']) * 100
        
        result.append({
            'id': problem['id'],
            'title': problem['title'],
            'difficulty': problem['difficulty'],
            'pass_rate': round(pass_rate, 2)
        })
    
    db.close()
    return result

@router.get("/problems/{problem_id}")
def get_problem(problem_id: int, current_user: dict = Depends(get_current_user)):
    db = get_db()
    problem = db.execute('SELECT * FROM problems WHERE id = ?', (problem_id,)).fetchone()
    
    if not problem:
        raise HTTPException(status_code=404, detail="题目不存在")
    
    pass_rate = 0
    if problem['attempt_count'] > 0:
        pass_rate = (problem['pass_count'] / problem['attempt_count']) * 100
    
    result = {
        'id': problem['id'],
        'title': problem['title'],
        'difficulty': problem['difficulty'],
        'description': problem['description'],
        'input_format': problem['input_format'],
        'output_format': problem['output_format'],
        'sample_inputs': json.loads(problem['sample_inputs']),
        'sample_outputs': json.loads(problem['sample_outputs']),
        'constraints': problem['constraints'],
        'time_complexity': problem['time_complexity'],
        'space_complexity': problem['space_complexity'],
        'max_time_complexity': problem['max_time_complexity'],
        'max_space_complexity': problem['max_space_complexity'],
        'pass_rate': round(pass_rate, 2)
    }
    
    db.close()
    return result

@router.post("/problems/{problem_id}/submit")
def submit_code(problem_id: int, code: str, current_user: dict = Depends(get_current_user)):
    db = get_db()
    problem = db.execute('SELECT * FROM problems WHERE id = ?', (problem_id,)).fetchone()
    
    if not problem:
        raise HTTPException(status_code=404, detail="题目不存在")
    
    test_cases = json.loads(problem['test_cases'])
    results, errors = execute_python_code(code, test_cases)
    
    passed_count = sum(1 for r in results if r['passed'])
    total_count = len(results)
    
    user_problem = db.execute('SELECT * FROM user_problems WHERE user_id = ? AND problem_id = ?',
                             (current_user['id'], problem_id)).fetchone()
    
    if user_problem:
        db.execute('UPDATE user_problems SET attempts = attempts + 1 WHERE user_id = ? AND problem_id = ?',
                   (current_user['id'], problem_id))
    else:
        db.execute('INSERT INTO user_problems (user_id, problem_id, attempts) VALUES (?, ?, 1)',
                   (current_user['id'], problem_id))
        db.execute('UPDATE problems SET attempt_count = attempt_count + 1 WHERE id = ?', (problem_id,))
    
    all_passed = passed_count == total_count
    
    if all_passed:
        time_complexity, space_complexity = analyze_complexity(code)
        
        time_ok = compare_complexity(time_complexity, problem['max_time_complexity'])
        space_ok = compare_complexity(space_complexity, problem['max_space_complexity'])
        
        if time_ok and space_ok:
            status = "通过"
            
            if not user_problem or user_problem['passed'] == 0:
                db.execute('UPDATE user_problems SET passed = 1 WHERE user_id = ? AND problem_id = ?',
                           (current_user['id'], problem_id))
                db.execute('UPDATE problems SET pass_count = pass_count + 1 WHERE id = ?', (problem_id,))
        else:
            status = "未通过"
            if not time_ok:
                errors.append(f"当前算法时间复杂度为{time_complexity}，题目要求为{problem['max_time_complexity']}，时间复杂度过高，测试未通过")
            if not space_ok:
                errors.append(f"当前算法空间复杂度为{space_complexity}，题目要求为{problem['max_space_complexity']}，空间复杂度过高，测试未通过")
    else:
        status = "未通过"
        time_complexity = None
        space_complexity = None
    
    db.execute('INSERT INTO submissions (user_id, problem_id, code, status, passed_test_cases, total_test_cases, time_complexity, space_complexity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
               (current_user['id'], problem_id, code, status, passed_count, total_count, time_complexity, space_complexity))
    
    db.commit()
    db.close()
    
    return {
        'status': status,
        'passed': passed_count,
        'total': total_count,
        'errors': errors,
        'time_complexity': time_complexity,
        'space_complexity': space_complexity
    }