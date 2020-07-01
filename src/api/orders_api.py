from flask import Flask, request, render_template

import functools
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.Orders import Orders
from src.logic_processor.order_products_processor import OPP
from src.database.db import db_session

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')


@orders_bp.route('/insert_orders',methods=['POST'])
def insert_orders():
    custumer_id = request.json.get("customer_id")
    shopkeeper_id = request.json.get('shopkeeper_id')
    total_order_price= request.json.get('total_order_price')
    negotiated_price= request.json.get('negotiated_price')
    transported_point=request.json.get('transported_point')
    bilty_no=request.json.get('bilty_no')
    order_status=request.json.get('order_status')
    import datetime
    date = datetime.datetime.now()
    b = Orders(custumer_id, shopkeeper_id, date, total_order_price,negotiated_price,transported_point,bilty_no,
              order_status)
    res = OPP.process_insert_orders(b)
    return res

@orders_bp.route("/list_orders",methods=['POST'])
def list_orders():
    u = Orders.query.all()
    ul = [us.toDict() for us in u]
    return json.dumps(ul)

@orders_bp.route('/update_order',methods=['POST'])
def update_order():
    return OPP.update_order(request.get_json())



