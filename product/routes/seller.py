from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from ..import schemas
from ..import models
from passlib.context import CryptContext

router = APIRouter(tags=['Seller'])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/seller', status_code=status.HTTP_201_CREATED, response_model = schemas.DisplaySeller)
def createSeller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashedpassword = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashedpassword)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller