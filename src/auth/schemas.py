from pydantic import BaseModel, EmailStr, Field, validator
from typing import Pattern
import re

from src.blogs.models import Blog


class UserBase(BaseModel):
    f_name: str = Field(max_length=200, title='dsmsom')
    l_name: str = Field(max_length=200)
    phone: str = Field(pattern=r"^09\d{2}\s*?\d{3}\s*?\d{4}$")
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(
        min_length=6,
    )

    @validator('password')
    def validate_password(cls, value):
        if not re.search(r'\d', value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r'[A-Z]', value):
            raise ValueError(
                "Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', value):
            raise ValueError(
                "Password must contain at least one lowercase letter")
        if not re.search(r'[#$%@&]', value):
            raise ValueError(
                "Password must contain at least one special character (#$%@&)")
        if not 6 <= len(value) <= 250:
            raise ValueError(
                "Password must be between 6 and 250 characters long")

        return value


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
