"""
@author: kongwiki
@file:   __init__.py.py
@time:   19-1-8下午7:01
@contact: kongwiki@163.com
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors