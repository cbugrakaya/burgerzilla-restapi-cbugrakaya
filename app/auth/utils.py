from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length


class LoginSchema(Schema):
    """ /auth/customer/login 
        /auth/restaurant/login 
        [POST]

    Parameters:
    - Email
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])


class CustRegisterSchema(Schema):
    """ /auth/customer/register[POST]

    Parameters:
    - Email
    - Fullname (Str)
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    fullname = fields.Str(
        required=True,
        validate=[
            Regexp(
                r"^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$", error="Invalid name!",
            )
        ]
    )
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])



class ResRegisterSchema(Schema):
    """ /auth/customer/register 
        /auth/restaurant/register
        [POST]

    Parameters:
    - Email
    - Fullname (Str)
    - Password (Str)
    - Restaurant Name (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    fullname = fields.Str(
        required=True,
        validate=[
            Regexp(
                r"^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$", error="Invalid name!",
            )
        ]
    )
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])
    restaurant_name = fields.Str(required=True, validate=[Length(min=4, max=128)])