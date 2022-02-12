from flask import request
from flask_restx import Resource
from app.utils import validation_error

from .service import AuthCustService, AuthResService
from .dto import AuthDto
from .utils import LoginSchema, CustRegisterSchema, ResRegisterSchema

api = AuthDto.api
auth_success = AuthDto.auth_success

# Customer and Restaurant ogin schema is the same
login_schema = LoginSchema()

# Customer register schema 
cust_register_schema = CustRegisterSchema()

# Restaurant register schema
res_register_schema = ResRegisterSchema()

@api.route("/customer/login")
class AuthCustLogin(Resource):
    """
    Customer Login Endpoint
    Customer requests a token to be used in future requests
    """
    auth_login = AuthDto.auth_login
    @api.doc("Auth Customer Login",responses = {200: "Success", 400: "Validation Error",403: "Invalid Credentials",404: "User Not Found", 405:"Method Not Allowed"})
    @api.expect(auth_login, validate=True)
    def post(self):
        """
        Customer Login
        """
        login_data = request.get_json()

        # Validate login data
        if (errors := login_schema.validate(login_data)):
            return validation_error(False,errors),400
        return AuthCustService.login(login_data)

@api.route("/customer/register")
class AuthCustRegister(Resource):
    """
    Customer Registration Endpoint
    Customer requests a token to be used in future requests
    """
    auth_register = AuthDto.auth_cust_register
    @api.doc("Auth Customer Register",responses = {200: "Success", 400: "Validation Error",409: "Email or Fullname already exists"})
    @api.expect(auth_register, validate=True)
    def post(self):
        """
        Customer Registration
        """
        register_data = request.get_json()

        # Validate register data
        if (errors := cust_register_schema.validate(register_data)):
            return validation_error(False,errors),400
        return AuthCustService.register(register_data)


@api.route("/restaurant/login")
class AuthResLogin(Resource):
    """
    Restaurant User Login Endpoint
    Restaurant User requests a token to be used in future requests
    """
    auth_login = AuthDto.auth_login
    @api.doc("Auth Restaurant Login",responses = {200: "Success", 400: "Validation Error",403: "Invalid Credentials",404: "User Not Found",405:"Method Not Allowed"})
    @api.expect(auth_login, validate=True)
    def post(self):
        """
        Restaurant Login
        """
        login_data = request.get_json()

        # Validate login data
        if (errors := login_schema.validate(login_data)):
            return validation_error(False,errors),400
        return AuthResService.login(login_data)

@api.route("/restaurant/register")
class AuthResRegister(Resource):
    """
    Restaurant User Registration Endpoint
    Restaurant User requests a token to be used in future requests
    """
    auth_register = AuthDto.auth_res_register
    @api.doc("Auth Restaurant Register",responses = {200: "Success", 400: "Validation Error",409: "Email or Fullname already exists",410:"Restaurant name already exists"})
    @api.expect(auth_register, validate=True)
    def post(self):
        """
        Restaurant Registration
        """
        register_data = request.get_json()

        # Validate register data
        if (errors := res_register_schema.validate(register_data)):
            return validation_error(False,errors),400
        return AuthResService.register(register_data)