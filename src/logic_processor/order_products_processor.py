from src.database.db import db_session
from src.models.Products import Products
from src.models.Brands import Brands
from src.models.Orders import Orders
from src.models.Products_In_Orders import Products_In_Orders
from src.dto.UserType import UserType
from flask import session
from src.logic_processor import constants
from src.logic_processor import common
from src.models.BankAccounts import Bankaccount
from src.models.ShopKeepers import ShopKeepers

###############################################################################
###############################################################################


class OrderProductsProcessor:

###############################################################################

    def process_insert_product(self, a: Products):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)

        validated = self.validate_product(a)
        if (validated != True):
            return validated

        if (a.image1):
            a.image1 = bytes(a.image1, 'utf-8')
        if (a.image2):
            a.image2 = bytes(a.image2, 'utf-8')
        if (a.image3):
            a.image3 = bytes(a.image3, 'utf-8')

        db_session.add(a)
        db_session.commit()
        return common.make_response_packet(0, "product inserted sucessfully", a.toDict())

###############################################################################

    def validate_product(self, a: Products):
        if (not a.product_name or not a.price or not a.image1 or not a.brand_id):
            return common.make_response_packet(6, "data is not valid", None)
        if (not common.is_number(a.price)):
            return common.make_response_packet(10, "Price is not valid number", None)
        brnd = Brands.query.filter(Brands.id == a.brand_id).first()
        if (brnd == None):
            return common.make_response_packet(11, "Brand does not exist", None)
        return True

###############################################################################

    def update_product(self, a):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not a['product_id']):
            return common.make_response_packet(14, "product id is required", None)
        prod = Products.query.filter(Products.id == a['product_id']).first()
        if (not prod):
            return common.make_response_packet(13, "Product Id not valid", None)

        keys = prod.__table__.columns
        updated = False
        for k in keys:
            updated |= common.check_and_update(prod, a, k.name)

        if updated:
            validated = self.validate_product(prod)
            if (validated != True):
                db_session.refresh(prod)
                return validated
            if ('image1' in a):
                prod.image1 = bytes(prod.image1, 'utf-8')
            if ('image2' in a):
                prod.image2 = bytes(prod.image2, 'utf-8')
            if ('image3' in a):
                prod.image3 = bytes(prod.image3, 'utf-8')
            db_session.commit()
            return common.make_response_packet(0, "product updated successfully", prod.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', prod.toDict())

###############################################################################

    def process_insert_brands(self, a: Brands):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not common.is_shopkeeper()):
            return common.make_response_packet(6, "you are not authorize to add brands", None)
        validated = self.validate_brands(a)
        if (validated !=True):
            return validated

        db_session.add(a)
        db_session.commit()
        return common.make_response_packet(2, "Brand inserted successfully", a.toDict())

###############################################################################

    def validate_brands(self,a:Brands):
        if (not a.shopkeeper_id or not a.brand_name):
           return common.make_response_packet(1, "data is not valid", None)
        return True


###############################################################################

    def update_brand(self, br):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if 'brand_id' not in br:
            return common.make_response_packet(5, 'brand id is required', None)
        brn = Brands.query.filter(Brands.id == br['brand_id']).first()
        if (not brn):
            return common.make_response_packet(6, 'brand_id is not valid', None)
        keys = brn.__table__.columns
        updated = False
        for k in keys:
            updated |= common.check_and_update(brn, br, k.name)
        if (updated):
            if (not common.is_shopkeeper()):
                return common.make_response_packet(6, "you are not authorize to add brands", None)
            if (not brn.shopkeeper_id or not brn.brand_name):
                return common.make_response_packet(1, "data is not valid", None)
            db_session.commit()
            return common.make_response_packet(0, "brand successfully updated", brn.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', brn.toDict())

###############################################################################

    def process_insert_orders(self, a: Orders):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not common.is_customer()):
            return common.make_response_packet(7, "you are not insert the order", None)
        validated = self.validate_order(a)
        if (validated != True):
            return validated

        db_session.add(a)
        db_session.commit()
        return common.make_response_packet(2, "Order Successfully Inserted", a.toDict())

###############################################################################

    def validate_order(self, a: Orders):
        if (not a.transported_point or not a.customer_id or not a.shopkeeper_id):
            return common.make_response_packet(3, "data is not valid", None)
        return True


###############################################################################

    def update_order(self, ord):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if 'order_id' not in ord:
            return common.make_response_packet(5, 'order id is required', None)
        orde = Orders.query.filter(Orders.id == ord['order_id']).first()
        if (not orde):
            return common.make_response_packet(6, 'order_id is not valid', None)
        keys = orde.__table__.columns
        updated = False
        for k in keys:
            updated |= common.check_and_update(orde, ord, k.name)
        if (updated):
            if (not orde.transported_point):
                db_session.refresh(orde)
                return common.make_response_packet(3, "data is not valid", None)
            db_session.commit()
            return common.make_response_packet(0, "order updated successfully", orde.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', orde.toDict())

###############################################################################

    def process_insert_product_in_orders(self, a: Products_In_Orders):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not common.is_customer()):
            return common.make_response_packet(7, "you are not insert the order", None)
        if (not a.quantity or not a.product_id or not a.order_id):
            return common.make_response_packet(3, "data is not valid", None)
        if (not common.is_number(a.quantity)):
            return common.make_response_packet(8, "Quanitity is not Valid", None)
        pd_id = Products.query.filter(Products.id == a.product_id).first()
        if (pd_id == None):
            return common.make_response_packet(9, "Product id is not found", None)
        od_id = Orders.query.filter(Orders.id == a.order_id).first()
        if (od_id == None):
            return common.make_response_packet(9, "Order id is not found", None)
        if not a.date:
            import datetime
            a.date = datetime.datetime.now()
        db_session.add(a)
        db_session.commit()
        return common.make_response_packet(0, "Process Order Successfully Placed", a.toDict())

###############################################################################

    def insert_bankcaccount(self, a: Bankaccount):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if (not common.is_customer()):
            return common.make_response_packet(7, "You are not a Customer", None)
        validated = self.validate_bankaccount(a)
        if (validated!=True):
            return validated

        db_session.add(a)
        db_session.commit()
        return common.make_response_packet(0, "Bank Account Successfully Inserted", None)

###############################################################################

    def validate_bankaccount(self,a:Bankaccount):
        if (not a.acount_no or not a.acount_holder_name or not a.bank_name):
            return common.make_response_packet(6, "Data is not Valid", None)
        return True
###############################################################################

    def update_bank(self, bnk):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if 'bank_id' not in bnk:
            return common.make_response_packet(5, 'Bank id is required', None)
        bank = Bankaccount.query.filter(Bankaccount.id == bnk['bank_id']).first()
        if (not bank):
            return common.make_response_packet(6, 'Bank_id is not valid', None)
        keys = bank.__table__.columns
        updated = False
        for k in keys:
            updated |= common.check_and_update(bank, bnk, k.name)
        if (updated):
            if (not bank.acount_no or not bank.acount_holder_name or not bank.bank_name):
                return common.make_response_packet(3, "data is not valid", None)
            db_session.commit()
            return common.make_response_packet(0, "Bank Information updated successfully", bank.toDict())
        else:
            return common.make_response_packet(1, 'Nothing Updated', bank.toDict())

###############################################################################

    def get_product_by_id(self,id):
        authentic = common.is_user_authenticated()
        if (not authentic):
            return common.make_response_packet(4, "User is not authenticated", None)
        if(not id):
            return common.make_response_packet(5, "Id is not valid", None)
        s = ShopKeepers.query.filter(ShopKeepers.id == id).first()
        if(not s):
            return common.make_response_packet(6,"Shopkeeper does not exist", None)
        res = Products.query.join(Brands).filter(Brands.shopkeeper_id == id).all()
        resList = [res1.toDict() for res1 in res]
        return common.make_response_packet(0,"",resList)

###############################################################################
###############################################################################


OPP = OrderProductsProcessor()
