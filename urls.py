# _*_ coding:utf-8 _*_

#import sae.const
from flask import Flask, jsonify
#from flaskext.sqlalchemy import SQLAlchemy
from flask import render_template
from myapp import app





#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, sae.const.MYSQL_PORT, sae.const.MYSQL_DB)
#db = SQLAlchemy(app)


from database import db

from models import User,Blog,Comment






@app.route('/')
def index():
    #admin3 = User(name='Test23', email='test@example.com32', password='123456789032', image='about:blank32')
    #db.session.add(admin3)
    #db.session.commit()
    admin = User.query.filter_by(name='Test').first()
    #users = User.query.all()
    #return render_template('test_users.html', users=users)
    blogs = Blog.query.all()
    return render_template('blog.html',blogs=blogs,user=admin)




@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return jsonify({'tasks': 'hh'})



@app.route('/api/users')
def api_get_users():
    users = User.query.all()
    # 把用户的口令隐藏掉:
    for u in users:
        u.password = '******'
    return u.name







