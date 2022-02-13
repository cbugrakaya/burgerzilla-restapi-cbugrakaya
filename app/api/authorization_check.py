from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity,get_jwt
from app.utils import message,err_resp, internal_err_resp

# this decorator is used to check if the user is logged as customer
def customer_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if claims['role'] != 'customer':
                return err_resp('This path for Customer ONLY!.',"unauthorized_401",401)
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# this decorator is used to check if the user is logged as restaurant
def restaurant_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if claims['role'] != 'restaurant':
                return err_resp('This path for Restaurant ONLY!.',"unauthorized_401",401)
            return fn(*args, **kwargs)
        return decorator
    return wrapper

