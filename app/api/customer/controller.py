from flask import current_app, request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from .service import CustomerService
from .dto import CustomerDto
from app.api import authorization_check

api = CustomerDto.api

# input data schema for order
order_ = CustomerDto.order

# input data schema to update order
order_update_customer = CustomerDto.order_update

# input data schema to create new order
order_new_data = CustomerDto.order_new_data

@api.route("/<int:order_id>")
class Order(Resource):

    @api.doc("get specific order", responses={
    200: ("Success",order_), 
    400: "Bad Request", 
    401: "Unauthorized", 
    404: "Not Found Order"})
    @jwt_required()
    @authorization_check.customer_required()
    def get(self, order_id):
        """Get specific order"""
        current_user = get_jwt_identity()
        return CustomerService.get_order(current_user,order_id)

    
    @api.doc("update specific order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    403: "Order Cancelled",
    404: "Not Found Order"})
    @api.expect(order_update_customer)
    @jwt_required()
    @authorization_check.customer_required()
    def put(self, order_id):
        """Update specific order"""
        update_data = request.get_json()
        current_user = get_jwt_identity()
        return CustomerService.update_order(current_user,order_id, update_data)


    @api.doc("cancel specific order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    402: "Order Already Cancelled",
    404: "Not Found Order"})
    @jwt_required()
    @authorization_check.customer_required()
    def delete(self, order_id):
        """Cancel specific order"""
        current_user = get_jwt_identity()
        return CustomerService.cancel_order(current_user,order_id)
    

@api.route("/orderlist")
class OrderList(Resource):
    @api.doc("get all orders", responses={
    200: ("Success"), 
    400: "Bad Request", 
    401: "Unauthorized", 
    404: "Not Found Any Order"})
    @jwt_required()
    @authorization_check.customer_required()
    def get(self):
        """Get all orders"""
        current_user = get_jwt_identity()
        return CustomerService.get_all_orders(current_user)


@api.route("/order/<int:restaurant_id>")
class OrderNew(Resource):
    @api.doc("create new order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Restaurant",
    405: "Not Found Product In This Restaurant"}
    )
    @api.expect(order_new_data)
    @jwt_required()
    @authorization_check.customer_required()
    def post(self, restaurant_id):
        """Create new order"""
        new_order_data = request.get_json()
        current_user = get_jwt_identity()
        return CustomerService.create_order(current_user,restaurant_id, new_order_data)
