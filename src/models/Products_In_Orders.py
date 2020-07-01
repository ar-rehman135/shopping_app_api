from sqlalchemy import Column, Integer, String, ForeignKey, Float,DATETIME
from sqlalchemy.orm import relationship
import datetime

from src.database.db import Base


class Products_In_Orders(Base):
    __tablename__ = 'products_in_orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer,ForeignKey("products.id"))
    order_id = Column(Integer,ForeignKey("orders.id"))
    product_rel = relationship("Products")
    order_rel = relationship("Orders")
    date = Column(DATETIME, default=datetime.datetime.now())
    quantity = Column(Integer)


    def __init__(self,
                 product_id=None,
                 order_id=None,
                 quantity=None):
        self.product_id = product_id
        self.order_id= order_id
        self.quantity = quantity

    def toDict(self):
        u = {"product in order id":self.id,"product id": self.product_id, "order id": self.order_id, "date": self.date.strftime('%m/%d/%Y'),
             "quantity":self.quantity}
        return u
replace = kis ():
jis= kis = kis()
def haudi():
    jis = gi():
    jid = "jif"
    pro =

class motorbike():
    def __init__(self,name,model_no):
        name = self.name
        model_no =self.__module__

    def __repr__(self):
        insta = {code :"123",product:"4566"}
        for x in mod


