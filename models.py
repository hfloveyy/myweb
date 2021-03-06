# _*_ coding:utf-8 _*_
from datetime import datetime
from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean, unique=True)
    name = db.Column(db.String(50), unique=True)
    image = db.Column(db.String(500))
    created_at = db.Column(db.DateTime)




class Blog(db.Model):
    """docstring for Blog"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(50), unique=True)
    user_image = db.Column(db.String(500))
    name = db.Column(db.String(50), unique=True)
    summary = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)





class Comment(db.Model):
    """docstring for Comment"""
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(50), unique=True)
    user_image = db.Column(db.String(500))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)




      

        









