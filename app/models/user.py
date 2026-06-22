from app.core.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    first_name = Column(String, unique= False, nullable= False)
    last_name = Column(String, unique= False, nullable= False)
    hashed_password = Column(String, nullable= False)
    cred_score = Column(Float, nullable=False,default=50)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))

