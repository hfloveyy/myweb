#coding=utf8

import sae.const
from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
import model




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, sae.const.MYSQL_PORT, sae.const.MYSQL_DB)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username






@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello_world2():
    return 'Hello World2!'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)