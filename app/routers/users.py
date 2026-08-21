from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse
from passlib.context import CryptContext
from jose import JWTError,jwt
from datetime import timedelta, datetime
import os
from fastapi.security import OAuth2PasswordBearer



# Constants for the folder
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SK")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
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


# The route for the user login
@router.post("/login", response_model=TokenResponse)
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    user_full = db.query(User).filter(User.email==user.email).first()


    if not user_full:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(user.password, user_full.hashed_password):
        raise HTTPException(status_code=404, detail="Incorrect password")

    access_token=create_access_token(
        data={"sub": str(user_full.id)},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return user

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user