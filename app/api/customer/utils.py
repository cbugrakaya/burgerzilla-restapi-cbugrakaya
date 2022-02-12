from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity,get_jwt
from app.utils import message,err_resp, internal_err_resp


# this decorator is used to check if the user is logged as customer
def customer_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if get_jwt()['role'] != 'customer':
            return err_resp('This path for Customer ONLY!.',"unauthorized_401",401)
        return fn(*args, **kwargs)
    return wrapper


# this decorator is used to check if the user is logged as 
def restaurant_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if get_jwt()['role'] != 'restaurant':
            return err_resp('This endpoint for Restaurant ONLY!',"unauthorized_401",401)
        return fn(*args, **kwargs)
    return wrapper