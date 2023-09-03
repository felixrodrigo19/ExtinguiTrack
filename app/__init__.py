from flask import Flask
from flask_restful import Api

from app import config
from app.resources.auth import Auth


def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    config.init_app(app, config_filename)
    api.add_resource(Auth, '/auth')

    return app
