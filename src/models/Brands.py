from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.database.db import Base


class Brands(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String(50))
    own_brand = Column(String(50))
    shopkeeper_id = Column(Integer, ForeignKey("shopkeepers.id"))
    shopkeeper_rel = relationship("ShopKeepers")

    def __init__(self,
                 brand_name=None,
                 shopkeeper_id=None,
                 own_brand = None
                 ):
        self.brand_name=brand_name
        self.own_brand = own_brand
        self.shopkeeper_id=shopkeeper_id

    def toDict(self):
        u = {"brand_id":self.id,"name":self.brand_name, "own_brand":self.own_brand}
        return u
#class Quality(Base):
 #   __tablename