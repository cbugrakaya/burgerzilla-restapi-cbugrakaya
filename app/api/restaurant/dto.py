from flask_restx import  Namespace, fields

class RestaurantDto:

    api = Namespace('restaurant', description='Restaurant related operations')




    data_resp = api.model('Restaurant data response', {
    "status": fields.Boolean,
    "message": fields.String,
    "access_token": fields.String,
    "user": fields.Nested("")

    })