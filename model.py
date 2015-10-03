# _*_ coding:utf-8 _*_
from flask import Flask
import sae.const
import mysql.connector 


conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)

db = web.database(
    dbn='mysql',
    host=sae.const.MYSQL_HOST,
    port=int(sae.const.MYSQL_PORT),
    user=sae.const.MYSQL_USER,
    passwd=sae.const.MYSQL_PASS,
    db=sae.const.MYSQL_DB
)
  
def add_contact(username, telnumber, unit):
    return db.insert('contacts', user=username, telnumber=telnumber, unit=unit)
  
def get_contact(name):
    myvar = dict(name=name)
    return db.select('contacts',myvar,where="name = $name")

def get_contact_telnumber(telnumber):
    return db.select('contacts', what=telnumber)

