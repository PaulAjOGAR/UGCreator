from datetime import datetime as dt

from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: int
    username: str
    trust_level: int
    account_status: int
    cred_score: float
    created_at: dt

class UserLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str