from src.database.db import db_session
from src.models.ShopKeepers import ShopKeepers
from src.models.Customers import Customers
from src.models.Products import Products
from src.dto.UserType import UserType
from flask import session
from sqlalchemy import and_
from src.logic_processor import constants
from src.logic_processor import common
from werkzeug.security import generate_password_hash, check_password_hash

class UserAccountsProcessor:

    def process_insert_shopkeeper(self,s):
        if(not s.user_name or not s.owner_name or  not s.shop_name or not s.owner_phone_no or not s.password or not s.address):
            return common.make_response_packet(6, "data is not valid", s.toDict())
        is_user_exist = ShopKeepers.query.filter(ShopKeepers.user_name == s.user_name).first() != None
        if(is_user_exist):
            return common.make_response_packet(7, "User name already in use", None)
        is_ownerphone_no_exist = ShopKeepers.query.filter(ShopKeepers.owner_phone_no == s.owner_phone_no).first() != None
        if (is_ownerphone_no_exist):
            return common.make_response_packet(7, "Phone number already in use", None)
        #is_shop_name_exist = ShopKeepers.query.filter(ShopKeepers.shop_name == s.shop_name).first() != None
        #if (is_shop_name_exist):
          #  return common.make_response_packet(7, "shop name already in use", None)
        s.password=generate_password_hash(s.password)
        db_session.add(s)
        db_session.commit()
        return common.make_response_packet(0, "shop keeper inserted successfully", s.toDict())


    def update_shopkeeper(self,s):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not s['shopkeeper_id']):
            return common.make_response_packet(5,'shopkeeper id is required',None)
        shop = ShopKeepers.query.filter(ShopKeepers.id== s['shopkeeper_id']).first()
        if (not shop):
            return common.make_response_packet(6,'shopkeeper_id is not valid',None)
        keys = shop.__table__.columns
        updated =False
        for k in keys:
            updated |= common.check_and_update(shop,s,k.name)
        if(updated):
            if(not shop.user_name or not shop.owner_name or  not shop.shop_name or not shop.owner_phone_no or not shop.password or not shop.address):
                return common.make_response_packet(6, "Data is not valid", None)
            is_user_exist = ShopKeepers.query.filter(and_(ShopKeepers.user_name == shop.user_name,ShopKeepers.id != shop.id)).first() != None
            if (is_user_exist):
                return common.make_response_packet(7, "User name already in use", None)
            #is_shop_name_exist = ShopKeepers.query.filter(and_(ShopKeepers.shop_name == shop.shop_name,ShopKeepers.id != shop.id)).first() != None
            #if (is_shop_name_exist):
              #  return common.make_response_packet(7, "shop name already in use", None)
            db_session.commit()
            return common.make_response_packet(0, "Shopkeeper updated successfully", shop.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', shop.toDict())




    def process_login(self,user_name,password,user_type):
        s = None
        if user_type == UserType.ShopKeeper:
            s = ShopKeepers.query.filter( ShopKeepers.user_name == user_name ).first()
        elif user_type == UserType.Customer:
            s = Customers.query.filter(Customers.customer_name == user_name).first()
        else:
            return common.make_response_packet(1, "Not valid user type", None)

        if(s == None):
            return common.make_response_packet(2,  "User Name Not Found", None)
        if(not check_password_hash(s.password,password)):
            return common.make_response_packet(3, "User Name or Password is Incorrect", None)
        session[constants.is_authenticated] = True
        session[constants.user_type] = user_type
        return  common.make_response_packet(0,"Login Successfully", None)

    def process_logout(self):
        session[constants.is_authenticated] = None
        session[constants.user_type] = None
        return common.make_response_packet(0,"logout successfully",None)

    def process_insert_customers(self, c: Customers):
        if (not c.user_name or not c.customer_name or not c.image or not c.cnic_no or not c.password or not c.customer_phone_no):
            return common.make_response_packet(6,"data is not valid",None)
        is_user_exist =Customers.query.filter(Customers.user_name == c.user_name).first() != None
        if (is_user_exist):
            return common.make_response_packet(7, "User name already in use", None)
        c.password=generate_password_hash(c.password)
        db_session.add(c)
        db_session.commit()
        return common.make_response_packet(0, "customer inserted successfully", c.toDict())

    def update_customer(self,c):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not 'customer_id' in c):
            return common.make_response_packet(5, 'customer id is required', None)
        cus = Customers.query.filter(Customers.id == c['customer_id']).first()
        if (not cus):
            return common.make_response_packet(6,'customer_id is not valid',None)
        keys = cus.__table__.columns
        updated = False
        for k in keys:
            updated |= common.check_and_update(cus,c, k.name)
        if (updated):
            if (not cus.user_name or not cus.customer_name or not cus.image or not cus.cnic_no or not cus.password or not cus.customer_phone_no):
                return common.make_response_packet(6, "Data is not valid", None)
            is_user_exist = Customers.query.filter(and_(Customers.user_name == cus.user_name, Customers.id != cus.id)).first() != None
            if (is_user_exist):
                db_session.refresh(cus)
                return common.make_response_packet(7, "User name already in use", None)
            db_session.commit()
            return common.make_response_packet(0, "customer updated successfully", cus.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', cus.toDict())

    def update_pass_cus(self,c):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not 'user_name' in c):
            return common.make_response_packet(5, 'user name is required', None)
        cus = Customers.query.filter(Customers.user_name == c['user_name']).first()
        if (not cus):
            return common.make_response_packet(6, 'user_name is not valid', None)
        if('old_password' not in c or 'new_password' not in c):
            return common.make_response_packet(21,"Data is not valid",None)
        correct = check_password_hash(cus.password,c['old_password'])
        if correct:
            cus.password = generate_password_hash(c['new_password'])
            db_session.commit()
            return common.make_response_packet(0, "Password Updated Successfully", cus.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', cus.toDict())

    def update_pass_shop(self,s):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not 'user_name' in s):
            return common.make_response_packet(5, 'User name is required', None)
        shop = ShopKeepers.query.filter(ShopKeepers.user_name == s['user_name']).first()
        if (not shop):
            return common.make_response_packet(6, 'user_name is not valid', None)
        if('old_password' not in s or 'new_password' not in s):
            return common.make_response_packet(21,"Data is not valid",None)
        correct = check_password_hash(shop.password,s['old_password'])
        if correct:
            issubclass(hifi,price,discount)
            {
                juf = id.__annotations__.id.not.
            }
            shop.password = generate_password_hash(s['new_password'])
            db_session.commit()
            return common.make_response_packet(0, "Password Updated Successfully", shop.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', shop.toDict())



UAP = UserAccountsProcessor()