from flask import Flask, request, render_template
from src.logic_processor.order_products_processor import OPP
import functools
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.Products_In_Orders import Products_In_Orders
from src.database.db import db_session

products_in_orders_bp = Blueprint('products_in_orders', __name__, url_prefix='/products_in_orders')


@products_in_orders_bp.route('/insert_products_in_orders',methods=['POST'])
def insert_products_in_orders():
    product_id = request.json.get("product_id")
    order_id = request.json.get("order_id")
    quantity = request.json.get("quantity")
    b = Products_In_Orders(product_id,order_id,quantity)
    res = OPP.process_insert_product_in_orders(b)
    return res

@products_in_orders_bp.route("/list_products_in_orders",methods=['POST'])
def list_products_in_orders():
    u = Products_In_Orders.query.all()
    ul = [us.toDict() for us in u]
    return json.dumps(ul)



