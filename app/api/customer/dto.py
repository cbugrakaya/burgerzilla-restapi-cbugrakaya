from flask_restx import  Namespace, fields

class CustomerDto:

    api = Namespace('customer', description='Customer related operations')

    order = api.model('Order', {
        'order_id': fields.Integer(required=True, description='The order unique identifier'),
        'user_id': fields.Integer(required=True, description='The user unique identifier'),
        'product_ids': fields.String(required=True, description='The product ids'),
        'quantities': fields.String(required=True, description='The quantities'),
        'order_date': fields.DateTime(required=True, description='The order date'),
        'order_status': fields.String(required=True, description='The order status')
    })  
    

    orders_data_response = api.model('Order Data Response', {
        'order_id': fields.Integer(required=True, description='The order unique identifier'),
        'user_id': fields.Integer(required=True, description='The user unique identifier'),
        'orders':  fields.List(fields.Nested(order))
    })


    order_update = api.model('Order Update Data', {
        'quantities': fields.Integer(required=True, description="Quantities")
    })

    order_new_data = api.model('Order New Data', {
        # 'product_ids': fields.List(fields.Integer, required=True, description="Product IDs"),
        # 'quantities': fields.List(fields.Integer, required=True, description="Quantities")
        'product_ids': fields.Integer(required=True, description="Product IDs"),
        'quantities': fields.Integer(required=True, description="Quantities")
    })