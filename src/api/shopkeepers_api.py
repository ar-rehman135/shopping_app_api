from flask import Flask, request, render_template
import functools
from src.logic_processor import common
from src.logic_processor.user_accounts_processor import UAP
from src.logic_processor.order_products_processor import OPP
import json
from src.dto.UserType import UserType
from werkzeug.utils import secure_filename
import os
import base64
import uuid

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.ShopKeepers import ShopKeepers


shopkeeper_bp = Blueprint('shopkeeper', __name__, url_prefix='/shopkeeper')


#shopkeeper_bp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@shopkeeper_bp.route('/insert_shopkeeper',methods=['POST'])
def insert_shop_keeper():
    user_name = request.json.get('user_name')
    shop_name = request.json.get('shop_name')
    owner_name = request.json.get('owner_name')
    owner_phone_no = request.json.get('owner_phone_no')
    password = request.json.get('password')
    address = request.json.get('address')
    shop_phone_no1 = request.json.get('shop_phone_no1')
    shop_phone_no2 = request.json.get('shop_phone_no2')
    loc_long = request.json.get('loc_long')
    loc_lat = request.json.get('loc_lat')
    image = request.json.get('image')
    email  = request.json.get('email')
    s = ShopKeepers(user_name,shop_name,password,owner_name,owner_phone_no,shop_phone_no1,shop_phone_no2,loc_long,loc_lat,address,image,email)
    res = UAP.process_insert_shopkeeper(s)
    return res

@shopkeeper_bp.route("/update_shopkeeper",methods=['POST'])
def update_shopkeeper():
    return UAP.update_shopkeeper(request.json)

@shopkeeper_bp.route("/list_shopkeepers",methods=['POST'])
def list_shopkeeper():
    u = ShopKeepers.query.all()
    ul = [us.toDict() for us in u]
    return json.dumps(ul)

@shopkeeper_bp.route("/login",methods=['POST'])
def login_shopkeeper():
    user_name = request.json.get('user_name')
    password = request.json.get('password')
    return UAP.process_login(user_name,password,UserType.ShopKeeper)


@shopkeeper_bp.route("/logout",methods=['POST'])
def logout_shopkeeper():
    return UAP.process_logout()

@shopkeeper_bp.route("/update_password",methods=['POST'])
def update_password():
    return UAP.update_pass_shop(request.json)



@shopkeeper_bp.route("/upload_file",methods=['GET','POST'])
def fileUpload():
    target = os.path.abspath("static/")
    user_profile_direc = os.path.join(target,"user")
    print(target)
    print(user_profile_direc)
    if not os.path.isdir(user_profile_direc):
        os.mkdir(user_profile_direc)
    #logger.info("welcome to upload`")
    file = request.json
    f = file['file_attachement']
    #print(f)
    f = bytes(f,'utf-8')

    #filename = secure_filename(file.filename)

    #imgdata = base64.b64decode(f)
    filename = uuid.uuid1().hex
    destination = "/".join([user_profile_direc, filename])
    print(destination)
    with open(destination + ".jpg", "wb") as fh:
        fh.write(base64.decodebytes(f))
    #file.save(destination)
    #session['uploadFilePath'] = destination
    response = "Whatever you wish too return"
    return common.make_response_packet(1, 'Incorrect Old Password', 'Server Data')



