from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.database import get_db
from app.security import verify_password, get_password_hash, create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models import UserCreate, UserLogin

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    db = get_db()
    
    existing_user = db.execute('SELECT * FROM users WHERE username = ? OR email = ?', 
                              (user.username, user.email)).fetchone()
    if existing_user:
        raise HTTPException(status_code=400, detail="用户名或邮箱已存在")
    
    password_hash = get_password_hash(user.password)
    
    db.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
               (user.username, user.email, password_hash))
    db.commit()
    db.close()
    
    return {"message": "注册成功"}

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (form_data.username,)).fetchone()
    
    if not user or not verify_password(form_data.password, user['password_hash']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['username']}, expires_delta=access_token_expires
    )
    
    db.close()
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return {
        "id": current_user['id'],
        "username": current_user['username'],
        "email": current_user['email'],
        "avatar_url": current_user['avatar_url'],
        "bio": current_user['bio']
    }