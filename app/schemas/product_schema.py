from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_name: str
    category: str
    price: float
    stock: int
    size: str
    description: str
    image_url: str

class ProductResponse(ProductCreate):
    id: int
    class Config:
        from_attributes =True

