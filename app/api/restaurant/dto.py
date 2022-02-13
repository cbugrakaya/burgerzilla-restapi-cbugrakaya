from email.policy import default
from itertools import product
from flask_restx import  Namespace, fields

class RestaurantDto:

    api = Namespace('restaurant', description='Restaurant related operations')

    restaurant_object = api.model('Restaurant Object', {
        'id': fields.Integer(readOnly=True, description='The unique identifier of a restaurant'),
        'name': fields.String(required=True, description='Restaurant name')
    })

    order_status_update_data = api.model('Order Status Update Data', {
        'status': fields.Integer(required=True, description='Order status NEW = 1, PREPARING = 2, ONTHEWAY = 3, DELIVERED = 4, CUSTOMER_CANCELLED = 5, RESTAURANT_CANCELLED = 6')
    })

    product_update_data = api.model('Product Update Data', {
        'product_name': fields.String(description='Product name'),
        'product_price': fields.Float(description='Product price'),
        'product_description': fields.String(description='Product description'),
        'product_image_url': fields.String(description='Product image url')
    })

    product_new_data = api.model('Product New Data', {
        'product_name': fields.String(required=True, description='Product name'),
        'product_price': fields.Float(required=True, description='Product price'),
        'product_description': fields.String(required=True, description='Product description'),
        'product_image_url': fields.String(required=True, description='Product image url')
    })

    order_data = api.model('Order Data', {
        'order_id': fields.Integer(readOnly=True, description='The unique identifier of a order'),
        'user_id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
        'product_ids': fields.List(fields.Integer, description='List of product ids'),
        'quantities': fields.List(fields.Integer, description='List of quantities'),
        'order_date': fields.DateTime(readOnly=True, description='Order date'),
        'order_status': fields.String(readOnly=True, description='Order status NEW = 1, PREPARING = 2, ONTHEWAY = 3, DELIVERED = 4, CUSTOMER_CANCELLED = 5, RESTAURANT_CANCELLED = 6')
    })

    data_resp = api.model('Restaurant data response', {
    "status": fields.Boolean,
    "message": fields.String,
    "access_token": fields.String,
    "order": order_data
    })