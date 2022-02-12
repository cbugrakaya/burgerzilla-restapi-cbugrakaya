from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


from .service import RestaurantService
from .dto import RestaurantDto

api = RestaurantDto.api
data_resp = ""