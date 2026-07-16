from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

#login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str    

#JWT response
class Token(BaseModel):
    access_token: str
    token_type: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None 
    completed: bool

class TaskResponse(BaseModel):  
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True  