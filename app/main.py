from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.user import User
from app.models.product import Product
from app.models.review import Review
from app.routers.users import router as users_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "UGC Platform is running"}

