# _*_ coding:utf-8 _*_

from flask import Flask
from flask.ext.restful import Api, Resource, fields, marshal_with
from myapp import app
from models import User,Blog,Comment


api = Api(app)


user_fields = {
    'name': fields.String,
    'password': fields.String, 
}


class UserAPI(Resource):
    @marshal_with(user_fields, envelope='resource')
    def get(self, id):
        admin = User.query.filter_by(id=id).first()
        return admin

    def put(self, id):
        pass

    def delete(self, id):
        pass


        

class AllUserAPI(Resource):
    @marshal_with(user_fields, envelope='resources')
    def get(self, **kwargs):
        users = User.query.all()
        return users

    def put(self, id):
        pass




api.add_resource(AllUserAPI, '/api/users', endpoint = 'users')
api.add_resource(UserAPI, '/api/users/<int:id>', endpoint = 'user')