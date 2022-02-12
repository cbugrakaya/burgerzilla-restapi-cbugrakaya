from flask_restx import  Namespace, fields

class CustomerDto:

    api = Namespace('customer', description='Customer related operations')


    order_update_data = api.model('Login Data', {
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password")
    })

    order_new_data = api.model('New Order Data', {
        "res_id": fields.Integer(required=True, description="Restaurant ID"),
        #"product_id": fields.Integer(required=True, description="Product ID"),
        'product_ids': fields.List(fields.Integer, required=True, description="Product IDs"),
        #"quantity": fields.Integer(required=True, description="Quantity"),
        'quantities': fields.List(fields.Integer, required=True, description="Quantities"),
    })