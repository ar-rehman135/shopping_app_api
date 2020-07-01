from flask import Flask, request, render_template

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

home_bp = Blueprint('home', __name__, url_prefix='/')


@home_bp.route('/', methods=['GET'], defaults={'path': ''})
@home_bp.route('/<path:path>', methods=['GET'])
def catch_all(path):
    return render_template("index.html")

