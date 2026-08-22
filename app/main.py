from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.user import User
from app.models.product import Product
from app.models.review import Review
from app.routers.users import router as users_router
from app.routers.products import router as products_router
from app.routers.reviews import router as reviews_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
app.include_router(users_router)
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(reviews_router, prefix="/reviews", tags=["reviews"])

@app.get("/")
def read_root():
    return {"message": "UGC Platform is running"}

