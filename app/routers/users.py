from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from passlib.context import CryptContext



router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate,db: Session = Depends(get_db)):
    e_user=db.query(User).filter(User.email== user.email).first()
    u_user=db.query(User).filter(User.username== user.username).first()



    if e_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    elif u_user:
        raise HTTPException(status_code=400, detail="Username has been taken")

    hashed_password = pwd_context.hash(user.password)

    new_user = User(
        email= user.email,
        username= user.username,
        first_name = user.first_name,
        last_name = user.last_name,
        hashed_password = hashed_password

    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
