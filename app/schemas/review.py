from pydantic import BaseModel
from datetime import datetime as dt

class ReviewCreate(BaseModel):
    product_id: int
    body: str
    rating: int

class ReviewResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    body:str
    rating: int
    guideline_score: float
    approved: bool
    created_at: dt