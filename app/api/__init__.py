from flask_restx import Api
from flask import Blueprint

from .customer.controller import api as customer_ns
from .restaurant.controller import api as restaurant_ns

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version="1.0", title="Burgerzilla API", description="A REST-API micro-service that takes orders from hamburger restaurants, can view the status of the order, and enables transactions with the customer/restaurant authority regarding the order.")


api.add_namespace(restaurant_ns)
api.add_namespace(customer_ns)
