from flask import Flask, request, render_template

import functools
from src.logic_processor.order_products_processor import OPP
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.Products import Products
from src.database.db import db_session

product_bp = Blueprint('product', __name__, url_prefix='/product')


@product_bp.route('/insert_product',methods=['POST'])
def insert_product():
    product_name = request.json.get('product_name')
    image1 = request.json.get('image1')
    image2 = request.json.get('image2')
    image3 = request.json.get('image3')
    price =  request.json.get('price')
    product_des = request.json.get('product_des')
    brand_id = request.json.get('brand_id')
    p = Products(product_name,image1,image2,image3,price,product_des,brand_id)
    res = OPP.process_insert_product(p)
    return res


@product_bp.route('/update_product',methods=['POST'])
def update_product():
    return OPP.update_product(request.json)




@product_bp.route("/list_product",methods=['POST'])
def list_product():
    u = Products.query.all()
    ul = [us.toDict() for us in u]
    return json.dumps(ul)

@product_bp.route("/get_product_by_id",methods=['POST'])
def get_product_by_id():
    sid = request.json.get("shopkeeper_id")
    return OPP.get_product_by_id(sid)

