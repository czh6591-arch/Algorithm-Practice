from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    @field_validator('password')
    def password_length(cls, v):
        if len(v) < 8:
            raise ValueError('密码长度至少为8位')
        return v

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

class Problem(BaseModel):
    id: int
    title: str
    difficulty: str
    description: str
    input_format: str
    output_format: str
    sample_inputs: list
    sample_outputs: list
    constraints: str
    time_complexity: Optional[str] = None
    space_complexity: Optional[str] = None
    max_time_complexity: str
    max_space_complexity: str
    pass_rate: float

class Submission(BaseModel):
    problem_id: int
    code: str

class Tutorial(BaseModel):
    id: int
    category: str
    title: str
    content: str
    video_url: str