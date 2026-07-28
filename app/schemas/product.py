from pydantic import BaseModel
from datetime import datetime as dt

class ProductCreate(BaseModel):
    name: str
    description: str
    brand: str
    category:str

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    brand: str
    category: str
    avg_rating: float
    review_count: int
    created_at: dt