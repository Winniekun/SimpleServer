"""
@author: kongwiki
@file:   views.py
@time:   19-1-8下午7:22
@contact: kongwiki@163.com
"""

from app.main import main
from app.models import  User
from flask import request


@main.route('/')
def index():

    return "all is well"

@main.route('/user', methods=["POST", "GET"])
def checkUser():
    if request.method == "GET":
        return "理论上是成功的"
    haveregisted = User.query.filter_by(username=request.form['username']).all()
    if haveregisted:
        passwordRight = User.query.filter_by(username=request.form['username'],
                                             password=request.form['password']).all()

        if passwordRight:
            return "登录成功"

        else:
            return 1

    else:
        return 0

