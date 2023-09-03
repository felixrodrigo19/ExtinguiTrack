import os
import tomllib

from flask import Flask


def init_app(app: Flask, config_filename: str):
    app.config.from_file(config_filename, load=tomllib.load, text=False)
    app.config.update(SECRET_KEY=os.getenv('SECRET_KEY'))
