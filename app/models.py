"""
@author: kongwiki
@file:   models.py
@time:   19-1-8下午7:31
@contact: kongwiki@163.com
"""
from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return "<User %r>" % self.username

