from flask import Flask
from routes.user import user_blueprint

server = Flask(__name__)
server.config.from_object('config')

server.register_blueprint(user_blueprint)

if __name__ == '__main__':
    server.run()