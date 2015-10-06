# _*_ coding:utf-8 _*_

import re
from flask import Flask, jsonify, request

from flask import render_template
from myapp import app










from models import User,Blog,Comment

from apis import AllUserAPI,UserAPI,APIValueError,APIError




@app.route('/')
def index():
    #admin3 = User(name='Test23', email='test@example.com32', password='123456789032', image='about:blank32')
    #db.session.add(admin3)
    #db.session.commit()
    admin = User.query.filter_by(name='Test').first()
    blogs = Blog.query.all()
    return render_template('blog.html',blogs=blogs)


_RE_MD5 = re.compile(r'^[0-9a-f]{32}$')

@app.route('/register',methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        i = request.input(name='', email='', password='')
        name = i.name.strip()
        email = i.email.strip().lower()
        password = i.password
        if not name:
            raise APIValueError('name')
        if not email or not _RE_EMAIL.match(email):
            raise APIValueError('email')
        if not password or not _RE_MD5.match(password):
            raise APIValueError('password')
        user = User.query.filter_by(email=email).first()
        if user:
            raise APIError('register:failed', 'email', 'Email is already in use.')
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html',user=user)

















