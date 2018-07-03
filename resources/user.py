from flask_restful import Resource
import json

from models.user import UserModel

class GetUser(Resource):
    def get(self,name):
        print(name)
        
        return {'name': name} 

class PostUser(Resource):
    def post(self):
        user = UserModel()
        message = user.api_message()
        return message