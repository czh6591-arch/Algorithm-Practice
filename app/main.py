from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import auth, users, problems, tutorials
from app.database import init_db, get_db
import json

app = FastAPI(title="在线算法练习平台")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, tags=["users"])
app.include_router(problems.router, tags=["problems"])
app.include_router(tutorials.router, tags=["tutorials"])

@app.get("/")
def read_root():
    return FileResponse("app/templates/index.html")

@app.get("/login")
def login_page():
    return FileResponse("app/templates/login.html")

@app.get("/register")
def register_page():
    return FileResponse("app/templates/register.html")

@app.get("/profile")
def profile_page():
    return FileResponse("app/templates/profile.html")

@app.get("/problem/{problem_id}")
def problem_page(problem_id: int):
    return FileResponse("app/templates/problem.html")

@app.get("/tutorials-page")
def tutorials_page():
    return FileResponse("app/templates/tutorials.html")

if __name__ == "__main__":
    init_db()
    from app.init_data import init_data
    init_data()
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)