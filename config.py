import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    DEBUG = False

    # JWT CONFIG
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', os.urandom(24))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=2)


class DevelopmentConfig(Config):	
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL",'sqlite:///' + os.path.join(basedir, 'dev.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO =True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL",'sqlite:///' + os.path.join(basedir, 'test.sqlite'))
    #SQLALCHEMY_DATABASE_URI = "postgresql://dbuser1:123456@localhost:5432/restburger"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO =True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "data.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig,
)