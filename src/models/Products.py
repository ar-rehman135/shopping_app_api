from sqlalchemy import Column, Integer, String, ForeignKey, Float, BLOB
from sqlalchemy.orm import relationship

from src.database.db import Base


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(50))
    image1 = Column(BLOB)
    image2 = Column(BLOB)
    image3 = Column(BLOB)
    price = Column(Float)
    product_des = Column(String(150),nullable=True)
    brand_id = Column(Integer,ForeignKey("brands.id"))
    brand_rel = relationship("Brands")
    def __init__(self,
                 product_name=None,
                 image1=None,
                 image2=None,
                 image3=None,
                 price =None,
                 product_des= None,
                 brand_id = None,):
        self.product_name = product_name
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.price= price
        self.product_des = product_des
        self.brand_id = brand_id


    def toDict(self):
        u = {"product_id":self.id,"product_name":self.product_name,"image1": str(self.image1), "image2": str(self.image2), "image3": str(self.image3),
             "price":self.price,"product_des":self.product_des,"brand_id":self.brand_id}
        if(self.brand_rel):
            u["brand_name"] = self.brand_rel.brand_name
        return u
