from sqlalchemy import Column, Integer, String, ForeignKey, Float, BLOB,DATETIME
from sqlalchemy.orm import relationship
import  datetime
from src.models.Customers import Customers
from src.models.ShopKeepers import ShopKeepers

from src.database.db import Base


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    shopkeeper_id = Column(Integer, ForeignKey("shopkeepers.id"))
    date = Column(DATETIME,default=datetime.datetime.now())
    total_order_price = Column(Integer)
    negotiated_price = Column(Integer)
    transported_point=Column(String(100))
    bilty_no=Column(Integer)
    order_status=Column(Integer)
    customer_rel = relationship("Customers")
    shopkeeper_rel = relationship("ShopKeepers")

    def __init__(self,
                 customer_id=None,
                 shopkeeper_id=None,
                 date=None,
                 total_order_price=None,
                 negotiated_price=None,
                 transported_point=None,
                 bilty_no=None,
                 order_status=None):
        self.customer_id = customer_id
        self.shopkeeper_id= shopkeeper_id
        self.date=date
        self.total_order_price=total_order_price
        self.negotiated_price= negotiated_price
        self.transported_point = transported_point
        self.bilty_no = bilty_no
        self.order_status=order_status

    def toDict(self):
        u = {"order id ":self.id,"customer_id":self.customer_id,"Shop_keeper id": self.shopkeeper_id,
             "total order price":self.total_order_price,"negotiated price":self.negotiated_price,
             "transported point":self.transported_point,"bilty_no":self.bilty_no,"order_status":self.order_status}
        return u
