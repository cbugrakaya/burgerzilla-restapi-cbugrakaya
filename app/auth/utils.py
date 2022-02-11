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
    password = fields.Str(required=True, validate=[Length(min=5, max=128)])


class CustRegisterSchema(Schema):
    """ /auth/customer/register[POST]

    Parameters:
    - Email
    - Fullname (Str)
    - Password (Str)
    """

    email = fields.Email(
        required=True, 
        validate=[Length(max=64), Regexp(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",error="Invalid  email!")]
    )
    fullname = fields.Str(
        required=True, 
        validate=[
            Length(min=2, max=128)
            # Regexp(r"^[a-zA-ZğüşöçİĞÜŞÖÇ]+$",error="Invalid  name!")
        ]
    )
    password = fields.Str(required=True, validate=[Length(min=5, max=128)])



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

    email = fields.Email(
        required=True,  
        validate=[Length(max=64), Regexp(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",error="Invalid  email!")]
    )
    fullname = fields.Str(
        required=True,
        validate=[
            Length(min=2, max=128)
            # Regexp(r"^[a-zA-ZğüşöçİĞÜŞÖÇ]+$",error="Invalid  name!")
        ]
    )
    password = fields.Str(required=True, validate=[Length(min=5, max=128)])
    restaurant_name = fields.Str(required=True, validate=[Length(min=4, max=128)])