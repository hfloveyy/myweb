# _*_ coding:utf-8 _*_


from flask import Flask, jsonify

from flask import render_template
from myapp import app








from database import db

from models import User,Blog,Comment






@app.route('/')
def index():
    #admin3 = User(name='Test23', email='test@example.com32', password='123456789032', image='about:blank32')
    #db.session.add(admin3)
    #db.session.commit()
    admin = User.query.filter_by(name='Test').first()
    blogs = Blog.query.all()
    return render_template('blog.html',blogs=blogs,user=admin)




@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    users = User.query.all()
    # 把用户的口令隐藏掉:
    for u in users:
        u.password = '******'
    #return render_template('test_users.html', users=users)
    return jsonify(dict(users=users))



@app.route('/api/users')
def api_get_users():
    users = User.query.all()
    # 把用户的口令隐藏掉:
    for u in users:
        u.password = '******'
    #return render_template('test_users.html', users=users)
    return jsonify(dict(users=users))







