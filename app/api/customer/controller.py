from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from .service import CustomerService
from .dto import CustomerDto

api = CustomerDto.api


@api.route("/<int:order_id>")
class Order():

    # input data schema to update order
    order_update = CustomerDto.order_update_data
    
    @api.doc("get specific order", responses={
    200: ("Success"), 
    400: "Bad Request", 
    401: "Unauthorized", 
    404: "Not Found Order"})
    @jwt_required()
    # bir decarotor kullanıcı role kontrolü için
    def get(self, order_id):
        """Get specific order"""
        return CustomerService.get_order(order_id)

    
    @api.doc("update specific order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Order"})
    @api.expect(order_update)
    @jwt_required()
    def put(self, order_id):
        """Update specific order"""
        update_data = request.get_json()
        return CustomerService.update_order(order_id, update_data)

    @api.doc("delete specific order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Order"})
    @jwt_required()
    def delete(self, order_id):
        """Delete specific order"""
        return CustomerService.delete_order(order_id)
    

@api.route("/orderlist")
class OrderList():
    @api.doc("get all orders", responses={
    200: ("Success"), 
    400: "Bad Request", 
    401: "Unauthorized", 
    404: "Not Found Any Order"})
    @jwt_required
    def get(self):
        """Get all orders"""
        current_user = get_jwt_identity()
        return CustomerService.get_all_orders(current_user)

@api.route("/order/<int:restaurant_id>?<int:page>")
class OrderNew():

    # input data schema to create new order
    order_new_data = CustomerDto.order_new_data

    @api.doc("create new order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Restaurant"})
    @api.expect(order_new_data)
    @jwt_required
    def post(self, restaurant_id, page):
        """Create new order"""
        new_order_data = request.get_json()
        return CustomerService.create_order(restaurant_id, new_order_data, page)
