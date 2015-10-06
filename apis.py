# _*_ coding:utf-8 _*_

from flask import Flask
from flaskext.restful import Api, Resource, jsonify
from myapp import app

api = Api(app)



