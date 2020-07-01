from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.database.db import Base


class ShopKeepers(Base):
    __tablename__ = 'shopkeepers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(120), unique=True)
    owner_name = Column(String(50), unique=False)
    shop_name = Column(String(250), unique=False)
    owner_phone_no = Column(String(20), unique=True)
    shop_phone_no1 = Column(String(20))
    shop_phone_no2 = Column(String(20))
    loc_long = Column(Float)
    loc_lat = Column(Float)
    address = Column(String(250))
    password = Column(String(120))


    def __init__(self,
                 user_name = None,
                 shop_name=None,
                 password=None,
                 owner_name=None,
                 owner_phone_no=None,
                 shop_phone_no1=None,
                 shop_phone_no2=None,
                 loc_long=None,
                 loc_lat=None,
                 address=None):
        self.user_name = user_name
        self.shop_name = shop_name
        self.owner_name = owner_name
        self.owner_phone_no = owner_phone_no
        self.shop_phone_no1 = shop_phone_no1
        self.shop_phone_no2 = shop_phone_no2
        self.loc_long = loc_long
        self.loc_lat = loc_lat
        self.address = address
        self.password = password
        brands_rel = relationship("Brands")

    def __repr__(self):
        return '<User %r>' % (self.name)

    def toDict(self):
        u = {"username":self.user_name,"shopkeeper_id":self.id,"shop name": self.shop_name, "owner name": self.owner_name, "owner phone no": self.owner_phone_no}
        return u
