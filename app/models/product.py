from sqlalchemy import Column, Integer, String, Float

from app.database.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    size = Column(String(20))
    description = Column(String(500))
    image_url = Column(String(255))

