from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.product import Product
from app.models.user import User
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewResponse
from app.routers.users import get_db, get_current_user
from app.services.moderation import check_guidelines

router = APIRouter()

@router.post("/",response_model=ReviewResponse)
def create_review(review:ReviewCreate, current_user: User = Depends(get_current_user),db: Session = Depends(get_db)):
    existing = db.query(Review).filter(
        Review.user_id == current_user.id,
        Review.product_id == review.product_id
    ).first()
    product = db.query(Product).filter(Product.id == review.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail= "Product not found")

    if existing:
        raise HTTPException(status_code=400, detail="You have already reviewed this product")

    score, passed = check_guidelines(review.body)
    new_review= Review(
        product_id = review.product_id,
        body= review.body,
        user_id= current_user.id,
        rating = review.rating,
        guideline_score = score,
        approved=passed
    )



    new_total = product.avg_rating * product.review_count + review.rating
    new_count = product.review_count + 1
    new_avg = new_total / new_count

    db.add(new_review)
    product.avg_rating = new_avg
    product.review_count = new_count
    db.commit()
    db.refresh(new_review)
    return new_review

@router.get("/", response_model=list[ReviewResponse])
def get_reviews(db: Session = Depends(get_db)):
    reviews= db.query(Review).all()
    return reviews

@router.get("/{product_id}", response_model=list[ReviewResponse])
def get_product_reviews(product_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.product_id == product_id).all()


    return review