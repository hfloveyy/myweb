# _*_ coding:utf-8 _*_

import sae.const
from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy






app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, sae.const.MYSQL_PORT, sae.const.MYSQL_DB)
#db = SQLAlchemy(app)


from database import db

from models import User,Blog,Comment






@app.route('/')
def index():
    #admin3 = User(name='Test23', email='test@example.com32', password='123456789032', image='about:blank32')
    #db.session.add(admin3)
    #db.session.commit()
    admin = User.query.filter_by(name='admin').first()
    return admin.name

@app.route('/hello')
def hello_world2():
    return 'Hello World2!'



if __name__ == '__main__':
    app.run(debug=True)



