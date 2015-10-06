# _*_ coding:utf-8 _*_


from flask import Flask, jsonify

from flask import render_template
from myapp import app










from models import User,Blog,Comment

#from apis import AllUserAPI,UserAPI




@app.route('/')
def index():
    #admin3 = User(name='Test23', email='test@example.com32', password='123456789032', image='about:blank32')
    #db.session.add(admin3)
    #db.session.commit()
    admin = User.query.filter_by(name='Test').first()
    blogs = Blog.query.all()
    return render_template('blog.html',blogs=blogs,user=admin)



















