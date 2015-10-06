# _*_ coding:utf-8 _*_

from flask import Flask
from flask.ext.restful import Api, Resource, jsonify
from myapp import app
from models import User,Blog,Comment


api = Api(app)



class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

class AllUserAPI(Resource):
    def get(self, id):
        users = User.query.all()
        return users

    def put(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(AllUserAPI, '/api/users', endpoint = 'users')
api.add_resource(UserAPI, '/api/users/<int:id>', endpoint = 'user')