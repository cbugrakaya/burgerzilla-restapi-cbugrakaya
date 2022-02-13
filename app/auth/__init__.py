from flask_restx import Api
from flask import Blueprint

# from app.models.dataset import Dataset

from .controller import api as auth_ns

auth_bp = Blueprint('auth', __name__)


auth = Api(auth_bp, title='Authentication API', version='1.0',description='A REST-API micro-service that enables customers and restaurants to login and register.')

auth.add_namespace(auth_ns)