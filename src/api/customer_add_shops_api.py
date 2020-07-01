from flask import Flask, request, render_template

import functools
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.Customer_Add_Shops import Customer_Add_Shops
from src.database.db import db_session

customer_add_shops_bp = Blueprint('customer_add_shops', __name__, url_prefix='/customer_add_shops')


@customer_add_shops_bp.route('/insert_customer_add_shops',methods=['POST'])
def insert_customer_add_shops():
    customer_id = request.json.get("customer_id")
    shopkeeper_id = request.json.get("shopkeeper_id")
    creation_time = request.json.get("creation_time")
    modification_time = request.json.get("modification_time")

    import datetime
    creation_time = datetime.datetime.now()
    modification_time = datetime.datetime.now()
    b = Customer_Add_Shops(customer_id,shopkeeper_id,creation_time,modification_time)
    db_session.add(b)
    db_session.commit()
    return 'success'

@customer_add_shops_bp.route("/list_cusomer_add_shops",methods=['POST'])
def list_customer_add_shops():
    u = Customer_Add_Shops.query.all()
    ul = [us.toDict() for us in u]
    return json.dumps(ul)



