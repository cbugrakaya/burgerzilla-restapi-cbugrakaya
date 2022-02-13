"""

"""
from datetime import datetime
from email import message
from flask import current_app
from flask_jwt_extended import create_access_token

from app import db
import app
from app.utils import message,err_resp, internal_err_resp
from app.models.users import Users
from app.models.restaurant import Restaurant
from app.models.schemas import UsersSchema, RestaurantSchema

# User Schema to expose
user_schema = UsersSchema()
# Restaurant Schema to expose
restaurant_schema = RestaurantSchema()

# Customer Register and Login Service
class AuthCustService:
    @staticmethod
    def login(data):
        email = data.get('email')
        password = data.get('password')

        try:
            if not (user := Users.query.filter_by(email=email).first()):
                pass
                return err_resp('Email did not match any account.',"email_404",404)
            if user.role_type != "customer":
                pass
                return err_resp('This path is valid for Customer.',"user_type_405",405)
            elif user and user.verify_password(password):
                user_info = user_schema.dump(user)
                access_token = create_access_token(identity=user.id, additional_claims={'role': user.role_type})
                resp = message('True', 'Success Login!')
                resp['access_token'] = access_token
                resp['user'] = user_info

                current_app.logger.info(f'{user.fullname} (Customer) logged in at {datetime.now()}')
                return resp,200
            return err_resp('Email or Password is wrong.',"email_password_404",404)
            
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def register(data):
        email = data.get('email')
        fullname = data.get('fullname')
        password = data.get('password')
        
        if Users.query.filter_by(email=email).first():
            return err_resp('This email is already exists.',"email_409",409)
        elif Users.query.filter_by(fullname=fullname).first():
            return err_resp('This name is already exists.',"fullname_409",409)
        try:
            # customer created
            user = Users(email=email,
                            fullname=fullname,
                            password=password,
                            role_type="customer")
            db.session.add(user) # customer add to database
            db.session.commit() # commit to database

            user_info = user_schema.dump(user) # dump user data json format
            access_token = create_access_token(identity=user.id, additional_claims={'role': user.role_type}) # create token
            resp = message('True', 'Registration Successful!') # response message
            resp['access_token'] = access_token # add token to response
            resp['user'] = user_info # add user data to response

            current_app.logger.info(f'{user.fullname} (Customer) registered at {datetime.now()}')
            return resp,200 # return response

        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()


# Restaurant Register and Login Service
class AuthResService():
    @staticmethod
    def login(data):
        email = data.get('email')
        password = data.get('password')

        try:

            if not (user := Users.query.filter_by(email=email).first()):
                pass
                return err_resp('Email did not match any account',"email_404",404)
            if user.role_type != "restaurant":
                pass
                return err_resp('This path is valid for Restaurant.',"user_type_405",405)
            elif user and user.verify_password(password):
                user_info = user_schema.dump(user)
                res_id = Restaurant.query.filter_by(owner_id=user.id).first().id
                access_token = create_access_token(identity=user.id, additional_claims={'role': user.role_type,'res_id':res_id})
                resp = message('True', 'Success Login!')
                resp['access_token'] = access_token
                resp['user'] = user_info

                current_app.logger.info(f'{user.fullname} (Restaurant) logged in at {datetime.now()}')
                return resp,200
            return err_resp('Email or Password is wrong',"email_password_404",404)
  
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def register(data):
        email = data.get('email')
        fullname = data.get('fullname')
        password = data.get('password')
        restaurant_name = data.get('restaurant_name')

        if Users.query.filter_by(email=email).first():
            return err_resp('This email is already exists.',"email_409",409)
        elif Users.query.filter_by(fullname=fullname).first():
            return err_resp('This name is already exists.',"fullname_409",409)
        elif Restaurant.query.filter_by(restaurant_name=restaurant_name).first():
            return err_resp('This restaurant_name is already exists.',"restaurant_name_410",410)
        try:
            # restaurant and res owner created
            user = Users(email=email,
                            fullname=fullname,
                            password=password,
                            role_type="restaurant")
            db.session.add(user) # user add to database
            db.session.commit() # commit to database

            restaurant = Restaurant(restaurant_name=restaurant_name,owner_name=fullname,owner_id=user.id)
            db.session.add(restaurant) # restaurant add to database
            db.session.commit() # commit to database

            user_info = user_schema.dump(user) # dump user data json format
            restaurant_info = restaurant_schema.dump(restaurant)
            access_token = create_access_token(identity=user.id, additional_claims={'role': user.role_type,'res_id':restaurant.id}) # create token
            resp = message('True', 'Registration Successful!') # response message
            resp['access_token'] = access_token # add token to response
            resp['user'] = user_info # add user data to response
            resp['restaurant'] = restaurant_info # add restaurant data to response

            current_app.logger.info(f'{user.fullname} with {restaurant_name}(Restaurant Name) registered at {datetime.now()}')
            return resp,200 # return response

        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()