from flask import Flask
from flask import Blueprint
from flask_restful import Api

from resources.user import GetUser,PostUser

user_blueprint = Blueprint('user', __name__)
user_blueprint_api = Api(user_blueprint)

user_blueprint_api.add_resource(GetUser, '/user/<string:name>', methods = ['GET'])
user_blueprint_api.add_resource(PostUser, '/user', methods = ['POST'])