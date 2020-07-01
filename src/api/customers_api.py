from flask import Flask, request, render_template
from src.dto.UserType import UserType
import functools
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.Customers import Customers
from src.database.db import db_session
from src.logic_processor.user_accounts_processor import UAP

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')


@customers_bp.route('/insert_customers',methods=['POST'])
def insert_customers():
    user_name = request.json.get('user_name')
    customers_name = request.json.get('customer_name')
    shop_name = request.json.get('shop_name')
    customer_phone_no = request.json.get('customer_phone_no')
    shop_phone_no1 =request.json.get('shop_phone_no1')
    shop_phone_no2 =request.json.get('shop_phone_no2')
    loc_long =request.json.get('loc_long')
    loc_lat =request.json.get('loc_lat')
    address = request.json.get('address')
    cnic_no = request.json.get('cnic_no')
    password = request.json.get('password')
    image = request.json.get('image')
    s = Customers(user_name,customers_name,shop_name,customer_phone_no,shop_phone_no1,shop_phone_no2,loc_long,loc_lat,address,cnic_no,password,image)
    return UAP.process_insert_customers(s)

@customers_bp.route("/update_customer",methods=['POST'])
def update_customer():
    return UAP.update_customer(request.json)

@customers_bp.route("/list_customers",methods=['POST'])
def list_shopkeeper():
    u = Customers.query.all()
    ul = [us.toDict() for us in u]
    return json.dumps(ul)


@customers_bp.route("/login",methods=['POST'])
def login_shopkeeper():
    user_name = request.json.get('user_name')
    password = request.json.get('password')
    return UAP.process_login(user_name,password,UserType.Customer)

@customers_bp.route("/logout",methods=['POST'])
def logout_Customer():
    return UAP.process_logout()

@customers_bp.route("/update_password",methods=['POST'])
def update_password():
    return UAP.update_pass_cus(request.json)