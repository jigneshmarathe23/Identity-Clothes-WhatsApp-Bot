from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
    get_product_by_category
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product Not Found")

    return product

@router.put("/{product_id}",response_model=ProductResponse)
def update_product_details(
        product_id:int,
        product: ProductCreate,
        db:Session = Depends(get_db)
):
    updated_product = update_product(db,product_id,product)

    if updated_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )
    return updated_product

@router.delete("/{product_id}")

def delete_product_details(
        product_id :int,
        db:Session =Depends(get_db)
):
    deleted_product = delete_product(db,product_id)

    if deleted_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )
    return{
        "Message":"Product deleted Successfully !!!"
    }

@router.get("category/{category}",response_model=list[ProductResponse])
def get_category_products(
        category :str,
        db: Session = Depends(get_db)
):
    return get_product_by_category(db,category)