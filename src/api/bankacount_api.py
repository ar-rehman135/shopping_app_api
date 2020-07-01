from flask import Flask, request, render_template

import functools
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.BankAccounts import Bankaccount
from src.database.db import db_session
from src.logic_processor.order_products_processor import OPP
bankacount_bp = Blueprint('bankacount', __name__, url_prefix='/bankacount')


@bankacount_bp.route('/insert_bankacount',methods=['POST'])
def insert_bank_account():
    bank_name = request.json.get('bank_name')
    acount_holder_name = request.json.get('acount_holder_name')
    acount_no = request.json.get('acount_no')
    shopkeeper_id = request.json.get('shopkeeper_id')
    b = Bankaccount(bank_name,acount_holder_name,acount_no,shopkeeper_id)
    res = OPP.insert_bankcaccount(b)
    return res

@bankacount_bp.route("/list_bankacount",methods=['POST'])
def list_bankacount():
    u = Bankaccount.query.all()
    ul = [us.toDict() for us in u]
    return json.dumps(ul)

@bankacount_bp.route("/update_bankacount",methods=['POST'])
def update_bank():
    return OPP.update_bank(request.get_json())


