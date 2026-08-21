from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.routers.users import get_db, get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, current_user: User = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    product_name = db.query(Product).filter(Product.name == product.name).first()
    product_brand = db.query(Product).filter(Product.brand == product.brand).first()

    if product_name and product_brand:
        raise HTTPException(status_code=400, detail="Product already exists")

    new_product = Product(
        name=product.name,
        description=product.description,
        brand=product.brand,
        category=product.category,
        owner_id=current_user.id,

    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int,db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product