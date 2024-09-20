from fastapi import APIRouter, status, Response, HTTPException
from sqlalchemy.orm import Session
from fastapi.params import Depends
from typing import List
from product.routes.login import get_current_user
from ..database import get_db
from ..import schemas
from ..import models

router = APIRouter(tags=['Products'], prefix='/product')

@router.get('/', response_model = List[schemas.DisplayProduct])
def products(db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user)):
    products = db.query(models.Product).all()
    return products

@router.get('/{id}', response_model = schemas.DisplayProduct)
def product(id, response: Response, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user)):
    product = db.query(models.Product).filter(models.Product.id==id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    return product

@router.delete('/{id}')
def delete(id, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user)):
    db.query(models.Product).filter(models.Product.id==id).delete(synchronize_session=False)
    db.commit()
    return {'Product deleted'}

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Product, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user)):
    product = db.query(models.Product).filter(models.Product.id==id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {'Product updated'}

@router.post('/', status_code=status.HTTP_201_CREATED)
def add(request: schemas.Product, db: Session = Depends(get_db), current_user: schemas.Seller = Depends(get_current_user)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price, seller_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request
