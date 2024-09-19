from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List
from src.blogs.models import Tag, Blog


class TagBase(BaseModel):
    name: str = Field(max_length=200)


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int
    blogs: list[Blog] = []

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    content: str
    time_to_read: int = Field(gt=0, title="time to read in minute")


class BlogCreate(BlogBase):
    tags: list[TagCreate] = []


class Blog(BlogBase):
    id: int
    created_at: datetime
    user_id: int
    tags: list[Tag] = []

    class Config:
        orm_mode = True
