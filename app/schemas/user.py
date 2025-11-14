from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
