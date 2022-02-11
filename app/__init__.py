"""
APP initializer

"""
from re import A
from flask import Flask

from .extensions import cors, db, jwt, ma


# import config
from config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    register_extensions(app)

    # register blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .api import api_bp
    app.register_blueprint(api_bp,url_prefix='/api')

    return app

def register_extensions(app):

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    