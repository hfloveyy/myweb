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






class APIError(StandardError):
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)















api.add_resource(AllUserAPI, '/api/users', endpoint = 'users')
api.add_resource(UserAPI, '/api/users/<int:id>', endpoint = 'user')