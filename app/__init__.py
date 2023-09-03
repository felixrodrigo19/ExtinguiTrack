from flask import Flask

from app.ext import config


def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    config.init_app(app, config_filename)

    return app
