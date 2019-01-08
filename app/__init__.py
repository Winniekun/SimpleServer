"""
@author: kongwiki
@file:   __init__.py.py
@time:   19-1-8下午7:01
@contact: kongwiki@163.com
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config

moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)

    # 注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

