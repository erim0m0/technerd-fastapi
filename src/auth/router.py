from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from src.database import SessionLocal
from src.auth import schemas, models, service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db, user)
