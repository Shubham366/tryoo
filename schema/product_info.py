from sqlalchemy import Column, Integer, String, Float, Boolean
from config import Base  

class Product(Base):
    __tablename__ = "product_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)
    sku_id = Column(String)
    brand_name = Column(String)
    product_url = Column(String)
    product_big_img = Column(String)
    description = Column(String)
    price = Column(Float)
    current_price = Column(Float)
    promotion_price = Column(Float)
    discount_percentage = Column(Float)
    availability = Column(String)
    is_free_shipping = Column(String)
    rating_avg_value = Column(Float)
    venture_category_name_local = Column(String)
    venture_category2_name_en = Column(String)
    seller_name = Column(String)
    business_area = Column(String)
    business_type = Column(String)




