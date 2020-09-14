from flask import Flask, request, render_template

import functools
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.Brands import Brands
from src.database.db import db_session
from src.logic_processor.order_products_processor import OPP

brands_bp = Blueprint('brands', __name__, url_prefix='/brands')


@brands_bp.route('/insert_brands',methods=['POST'])
def insert_brands():
    brand_name = request.json.get('brand_name')
    shopkeeper_id = request.json.get('shopkeeper_id')
    own_brand = request.json.get("own_brand")
    #print("This is ownbrand",own_brand)
    b = Brands(brand_name,shopkeeper_id,own_brand)
    res =OPP.process_insert_brands(b)
    return res

@brands_bp.route("/list_brands",methods=['POST'])
def list_brands():
    return OPP.get_brands(request.get_json())



@brands_bp.route('/update_brand',methods=['POST'])
def update_brand():
    return OPP.update_brand(request.get_json())

@brands_bp.route('/delete_brand',methods=['POST'])
def delete_brand():
    return OPP.delete_brand(request.get_json())




