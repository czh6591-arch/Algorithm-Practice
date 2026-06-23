from fastapi import APIRouter
from app.database import get_db

router = APIRouter()

@router.get("/tutorials")
def get_tutorials(category: str = None):
    db = get_db()
    if category:
        tutorials = db.execute('SELECT * FROM tutorials WHERE category = ?', (category,)).fetchall()
    else:
        tutorials = db.execute('SELECT * FROM tutorials').fetchall()
    
    result = []
    for tutorial in tutorials:
        result.append({
            'id': tutorial['id'],
            'category': tutorial['category'],
            'title': tutorial['title'],
            'content': tutorial['content'],
            'video_url': tutorial['video_url']
        })
    
    db.close()
    return result

@router.get("/tutorials/{tutorial_id}")
def get_tutorial(tutorial_id: int):
    db = get_db()
    tutorial = db.execute('SELECT * FROM tutorials WHERE id = ?', (tutorial_id,)).fetchone()
    
    if not tutorial:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="教程不存在")
    
    result = {
        'id': tutorial['id'],
        'category': tutorial['category'],
        'title': tutorial['title'],
        'content': tutorial['content'],
        'video_url': tutorial['video_url']
    }
    
    db.close()
    return result