from sqlalchemy import Column, Integer, String, ForeignKey, Float,DATETIME
from sqlalchemy.orm import relationship

from src.database.db import Base
import datetime


class Customer_Add_Shops(Base):
    __tablename__ = 'customer_add_shops'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    shopkeeper_id = Column(Integer, ForeignKey("shopkeepers.id"))
    customer_rel = relationship("Customers")
    shopkeeper_rel = relationship("ShopKeepers")
    creation_time = Column(DATETIME,default=datetime.datetime.now())
    modification_time = Column(DATETIME,default=datetime.datetime.now())
    def __init__(self,
                 customer_id=None,
                 shopkeeper_id=None,
                 creation_time=None,
                 modification_time=None
                 ):
        self.customer_id= customer_id
        self.shopkeeper_id=shopkeeper_id
        self.creation_time=creation_time
        self.modification_time=modification_time


    def __repr__(self):
        return '<User %r>' % (self.name)

    def toDict(self):
        u = {"customer add shops":self.id,"customer id": self.customer_id, "shopkeeper id": self.shopkeeper_id, "creation time": self.creation_time,"modification time":self.modification_time}
        return u
