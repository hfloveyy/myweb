# _*_ coding:utf-8 _*_
from datetime import datetime
from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(50), unique=True)
    admin = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    image = db.Column(db.String(500), unique=True)
    created_at = db.Column(db.DateTime, unique=True)

    def __init__(self, email, password, admin, name, image, created_at):
        self.email = email
        self.password = password
        self.admin = admin
        self.name = name
        self.image = image
        self.created_at = created_at

class Blog(object):
    """docstring for Blog"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(50), unique=True)
    user_image = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    summary = db.Column(db.String(50), unique=True)
    content = db.Column(db.String(1000), unique=True)
    created_at = db.Column(db.DateTime, unique=True)
    def __init__(self, arg):
        super(Blog, self).__init__()
        self.arg = arg
        









