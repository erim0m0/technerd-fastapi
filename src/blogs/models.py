from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table

from src.database import Base

#  many-to-many relationship between Blog and Tag
blog_tag_association = Table(
    'blog_tag',
    Base.metadata,
    Column(
        'blog_id', Integer,
        ForeignKey('blogs.id')
    ),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    time_to_read = Column(Integer)
    content = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="blogs")

    tags = relationship(
        "Tag", secondary=blog_tag_association, back_populates="blogs"
    )


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    blogs = relationship(
        "Blog", secondary=blog_tag_association, back_populates="tags"
    )
