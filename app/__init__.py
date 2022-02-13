"""
APP initializer

"""
from re import A
from flask import Flask, current_app
from .extensions import cors, db, jwt, ma

import logging, os
from logging.handlers import RotatingFileHandler 

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
    
    
    if  not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/burgerzilla.log', maxBytes=10240,
                                    backupCount=10, encoding='utf-8')
        file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Burgerzilla REST API start')


    return app

def register_extensions(app):

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    