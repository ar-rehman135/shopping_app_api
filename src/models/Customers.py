from sqlalchemy import Column, Integer, String, ForeignKey, Float, BLOB
from sqlalchemy.orm import relationship

from src.database.db import Base


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(50), unique=False)
    shop_name = Column(String(250), unique=False)
    customer_phone_no = Column(String(20), unique=True)
    shop_phone_no1 = Column(String(20))
    shop_phone_no2 = Column(String(20))
    loc_long = Column(Float)
    loc_lat = Column(Float)
    address = Column(String(250))
    cnic_no = Column(String(20))
    image =Column(BLOB)
    password = Column(String(120))
    user_name = Column(String(120),unique=True)
    def __init__(self,
                 user_name=None,
                 customer_name=None,
                 shop_name=None,
                 customer_phone_no=None,
                 shop_phone_no1=None,
                 shop_phone_no2=None,
                 loc_long=None,
                 loc_lat=None,
                 address=None,
                 cnic_no=None,
                 password= None,
                 image= None,
                 ):
        self.customer_name = customer_name
        self.shop_name = shop_name
        self.customer_phone_no = customer_phone_no
        self.shop_phone_no1 = shop_phone_no1
        self.shop_phone_no2 = shop_phone_no2
        self.loc_long = loc_long
        self.loc_lat = loc_lat
        self.address = address
        self.cnic_no = cnic_no
        self.password = password
        self.image =  bytes(image,'utf-8')
        self.user_name=user_name
    def toDict(self):
        u = {"user_name":self.user_name,"customer_id":self.id,"customer name": self.customer_name, "shop name": self.shop_name, "customer phone no": self.customer_phone_no,
             "shop_phone no1":self.shop_phone_no1,"shop phone no2":self.shop_phone_no2,"latitude location":self.loc_lat,
             "longitude location":self.loc_long,"address":self.address,"cnic no":self.cnic_no,"password":self.password,"image": str(self.image)}
        return u
