from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product_schema import ProductCreate

def create_product(db:Session,product: ProductCreate):
    db_product =Product(
        product_name=product.product_name,
        category=product.category,
        price=product.price,
        stock=product.stock,
        size=product.size,
        description=product.description,
        image_url=product.image_url
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db:Session):
    return db.query(Product).all()

def get_product_by_id(db:Session,product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session,product_id: int,product:ProductCreate):
    db_product = get_product_by_id(db, product_id)

    if db_product is None:
        return  None

    db_product.product_name = product.product_name
    db_product.category = product.category
    db_product.price = product.price
    db_product.stock = product.stock
    db_product.size = product.size
    db_product.description = product.description
    db_product.image_url = product.image_url

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db:Session,product_id: int):
    db_product = get_product_by_id(db,product_id)
    if db_product is None:
        return None

    db.delete(db_product)
    db.commit()
    return db_product

def get_product_by_category(db: Session, category:str):
    return(
        db.query(Product)
        .filter(Product.category == category)
        .all()
    )