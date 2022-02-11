from flask_restx import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='Authentication related operations')


    user_obj = api.model('User Object', {
        "fullname": fields.String,
        "email": fields.String,
        "role_type": fields.String
    })

    auth_login = api.model('Login Data', {
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password")
    })

    auth_cust_register = api.model('Customer Register Data',{   
        "fullname": fields.String(required=True, description="User full name"),
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password"),
    })
               
    auth_res_register = api.model('Restaurant Register Data',{   
        "fullname": fields.String(required=True, description="User full name"),
        "email": fields.String(required=True, description="User email address"),
        "password": fields.String(required=True, description="User password"),
        "restaurant_name": fields.String(required=True, description="Restaurant name")
    })
                
    auth_success = api.model('Auth Success Response', 
    {"status": fields.Boolean,
     "message": fields.String,
     "access_token": fields.String,
     "user": fields.Nested(user_obj)
    })