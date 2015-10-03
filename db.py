#coding=utf8

import sae.const
from flaskext.sqlalchemy import SQLAlchemy
from . import app

app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, sae.const.MYSQL_PORT, sae.const.MYSQL_DB) 



db = SQLAlchemy(app)