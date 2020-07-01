import pytest
import json



################PRODUCTSVALIDATION#############

def test_OPP_validate_product_emptyCheck_nonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Products import Products
    p = Products()

    resp = OPP.validate_product(p)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_product_validCheck_ZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Products import Products
    p = Products("abc",bytearray('abc','utf-8'),None,None,121,None,1)

    resp = OPP.validate_product(p)


    assert resp == True

def test_OPP_validate_product_priceEmpty_nonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Products import Products
    p = Products("abc",bytearray('abc','utf-8'),None,None,None,None,1)

    resp = OPP.validate_product(p)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_product_nameEmpty_nonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Products import Products
    p = Products(None,bytearray('abc','utf-8'),1234,None,None,None,1)

    resp = OPP.validate_product(p)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_product_imageEmpty_nonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Products import Products
    p = Products("ABC",None,1234,None,None,None,1)

    resp = OPP.validate_product(p)
    resp = json.loads(resp)

    assert resp['status'] != 0


################ORDERSSVALIDATION#############

def test_OPP_validate_order_Empty_ZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Orders import Orders
    o = Orders()

    resp = OPP.validate_order(o)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_order_validCheck_ZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Orders import Orders
    p = Orders(1,1,'abc',2000,1000,'lahore',12,1)

    resp = OPP.validate_order(p)


    assert resp == True

def test_OPP_validate_order_transported_point_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Orders import Orders
    o = Orders(1,1,None,None,None,None,None,None)

    resp = OPP.validate_order(o)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_order_customer_id_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Orders import Orders
    o = Orders(None,1,None,None,None,'lahore',None,None)

    resp = OPP.validate_order(o)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_order_shopkeeper_id_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Orders import Orders
    o = Orders(1,None,None,None,None,'lahore',None,None)

    resp = OPP.validate_order(o)
    resp = json.loads(resp)

    assert resp['status'] != 0

################BANKACCOUNTVALIDATION#############

def test_OPP_validate_bankaccount_Empty_ZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.BankAccounts import Bankaccount
    b = Bankaccount()

    resp = OPP.validate_bankaccount(b)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_bankaccout_validCheck_ZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.BankAccounts import Bankaccount
    p = Bankaccount("HBL","Danish","PK-0123455",1)

    resp = OPP.validate_bankaccount(p)


    assert resp == True

def test_OPP_validate_bankaccount_account_no_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.BankAccounts import Bankaccount
    b = Bankaccount(None,"Danish",None,1)

    resp = OPP.validate_bankaccount(b)
    resp = json.loads(resp)

    assert resp['status'] != 0


def test_OPP_validate_bankaccount_account_holder_name_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.BankAccounts import Bankaccount
    b = Bankaccount("HBl",None,12345,1)

    resp = OPP.validate_bankaccount(b)
    resp = json.loads(resp)

    assert resp['status'] != 0


def test_OPP_validate_bankaccount_bank_name_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.BankAccounts import Bankaccount
    b = Bankaccount(None,"Danish",12345,1)

    resp = OPP.validate_bankaccount(b)
    resp = json.loads(resp)

    assert resp['status'] != 0


################BRANDSVALIDATION#############

def test_OPP_validate_Brands_Empty_ZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Brands import Brands
    b = Brands()

    resp = OPP.validate_brands(b)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_Brands_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Brands import Brands
    b = Brands("Diefei",1)

    resp = OPP.validate_brands(b)
    assert resp == True

def test_OPP_validate_Brands__brandname_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Brands import Brands
    b = Brands(None,1)

    resp = OPP.validate_brands(b)
    resp = json.loads(resp)

    assert resp['status'] != 0

def test_OPP_validate_Brands__shopkeeper_id_Empty_NonZeroStatus():
    from src.logic_processor.order_products_processor import OPP
    from src.database.db import init_db
    init_db()
    from src.models.Brands import Brands
    b = Brands("Diefei",None)

    resp = OPP.validate_brands(b)
    resp = json.loads(resp)

    assert resp['status'] != 0


if __name__ == '__main__':
    pytest.main()