from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from PIL import Image
import io
import os
from app.database import get_db
from app.security import get_current_user
from app.ocr import extract_text_from_image

router = APIRouter()

AVATAR_DIR = "app/static/avatars"
os.makedirs(AVATAR_DIR, exist_ok=True)

@router.put("/users/avatar")
async def update_avatar(file: UploadFile = File(...), current_user: dict = Depends(get_current_user)):
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        width, height = image.size
        
        if width < 64 or height < 64:
            raise HTTPException(status_code=400, detail="头像尺寸必须大于等于64x64")
        
        image = image.resize((64, 64))
        avatar_filename = f"avatar_{current_user['id']}.png"
        avatar_path = os.path.join(AVATAR_DIR, avatar_filename)
        image.save(avatar_path)
        
        db = get_db()
        db.execute('UPDATE users SET avatar_url = ? WHERE id = ?', 
                   (f"/static/avatars/{avatar_filename}", current_user['id']))
        db.commit()
        db.close()
        
        return {"message": "头像上传成功", "avatar_url": f"/static/avatars/{avatar_filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/users/bio")
async def update_bio(file: UploadFile = File(...), current_user: dict = Depends(get_current_user)):
    try:
        image_data = await file.read()
        text = extract_text_from_image(image_data)
        
        if not text:
            raise HTTPException(status_code=400, detail="当前图片未识别到文字，请重新上传")
        
        db = get_db()
        db.execute('UPDATE users SET bio = ? WHERE id = ?', (text, current_user['id']))
        db.commit()
        db.close()
        
        return {"message": "简介更新成功", "bio": text}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/users/bio/text")
def update_bio_text(bio: str, current_user: dict = Depends(get_current_user)):
    db = get_db()
    db.execute('UPDATE users SET bio = ? WHERE id = ?', (bio, current_user['id']))
    db.commit()
    db.close()
    return {"message": "简介更新成功", "bio": bio}