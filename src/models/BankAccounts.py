from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.models.ShopKeepers import ShopKeepers

from src.database.db import Base


class Bankaccount(Base):
    __tablename__ = 'bankaccount'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bank_name = Column(String(50), unique=False)
    acount_holder_name = Column(String(250), unique=False)
    acount_no = Column(String(30), unique=True)
    shopkeeper_id = Column(Integer,ForeignKey("shopkeepers.id"))
    shopkeeper_rel = relationship("ShopKeepers")

    def __init__(self,
                 bank_name=None,
                 acount_holder_name=None,
                 acount_no= None,
                 shopkeeper_id= None):
        self.bank_name = bank_name
        self.acount_holder_name =acount_holder_name
        self.acount_no =acount_no
        self.shopkeeper_id = shopkeeper_id

    def toDict(self):
        u = {"bank_name":self.bank_name,"acount_holder_name":self.acount_holder_name,"acount_no":self.acount_no}
        return u


    def product_in(self):
        prod = credits()
        property = delattr()
        prod = object
        def visit():
            for x in prod:
                x in y:
                break
                while():
                    if(True):
                    tuple()