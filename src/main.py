from fastapi import FastAPI

from src.database import Base, engine
from src.auth.router import router as auth_router
# from src.blogs.router import router as blogs_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
