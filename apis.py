# _*_ coding:utf-8 _*_

from flask import Flask, jsonify
from flask.ext.restful import Api, Resource
from myapp import app
from models import User,Blog,Comment


api = Api(app)



class UserAPI(Resource):
    def get(self, id):
        admin = User.query.filter_by(id=id).first()
        return admin

    def put(self, id):
        pass

    def delete(self, id):
        pass

class AllUserAPI(Resource):
    def get(self, id):
        users = User.query.all()
        if users is None:
            return 'None'
        else:
            return users

    def put(self, id):
        pass




api.add_resource(AllUserAPI, '/api/users', endpoint = 'users')
api.add_resource(UserAPI, '/api/users/<int:id>', endpoint = 'user')