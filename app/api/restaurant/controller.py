from flask import current_app, request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity,get_jwt

from .service import RestaurantService
from .dto import RestaurantDto
from app.api import authorization_check


api = RestaurantDto.api
order_status_update_data = RestaurantDto.order_status_update_data
data_resp = RestaurantDto.data_resp
product_update_data = RestaurantDto.product_update_data
product_new_data = RestaurantDto.product_new_data


@api.route('/<int:order_id>')
class ResOrder(Resource):
    
    @api.doc("get specific order", responses={
    200: ("Success"), 
    400: "Bad Request", 
    401: "Unauthorized", 
    404: "Not Found Order"})
    @jwt_required()
    @authorization_check.restaurant_required()
    def get(self, order_id):
        """Get specific order"""
        current_user = get_jwt()
        return RestaurantService.get_order(current_user['res_id'],order_id)    
    
    @api.doc("update specific order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    402: "Invalid status for order",
    403: "Order Cancelled",
    404: "Not Found Order"})
    @api.expect(order_status_update_data)
    @jwt_required()
    @authorization_check.restaurant_required()
    def put(self, order_id):
        """Update specific order status"""
        update_data = request.get_json()
        current_user = get_jwt()
        return RestaurantService.update_order(current_user['res_id'],order_id, update_data)

    @api.doc("cancel specific order", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Order"})
    @jwt_required()
    @authorization_check.restaurant_required()
    def delete(self, order_id):
        """Cancel specific order"""
        current_user = get_jwt()
        return RestaurantService.cancel_order(current_user['res_id'],order_id)




@api.route('/orderlist')
class ResOrderList(Resource):
        @api.doc("get all orders", responses={
        200: ("Success"), 
        400: "Bad Request", 
        401: "Unauthorized", 
        404: "Not Found Any Order"})
        @jwt_required()
        @authorization_check.restaurant_required()
        def get(self):
            """Get all orders"""
            current_user = get_jwt()
            return RestaurantService.get_all_orders(current_user['res_id'])


@api.route('/menu')
class ResMenu(Resource):

    @api.doc("get menu", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Restaurant"})
    @jwt_required()
    @authorization_check.restaurant_required()
    def get(self):
        """Get menu """
        current_user = get_jwt()
        return RestaurantService.get_menu(current_user['res_id'])
    
    # FIXME : This is not necessary or confusig
    # @api.doc("update menu", responses={
    # 200: ("Success"),
    # 400: "Bad Request",
    # 401: "Unauthorized",
    # 404: "Not Found Restaurant"})
    # @api.expect(product_update_data) 
    # @jwt_required()
    # @authorization_check.restaurant_required()
    # def put(self):
    #     """Update menu"""
    #     update_data = request.get_json()
    #     current_user = get_jwt()
    #     return RestaurantService.update_menu(current_user['res_id'],update_data)

    @api.doc("add product", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Restaurant"})
    @api.expect(product_new_data)
    @jwt_required()
    @authorization_check.restaurant_required()
    def post(self):
        """Add product"""
        data = request.get_json()
        current_user = get_jwt()
        return RestaurantService.add_product(current_user['res_id'],data)


@api.route('/menuProducts')
class ResMenuProductLıst(Resource):
    @api.doc("get all products", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found Any Product"})
    @jwt_required()
    @authorization_check.restaurant_required()
    def get(self):
        """Get all products"""
        current_user = get_jwt()
        return RestaurantService.get_all_products(current_user['res_id'])


@api.route('/menu/<int:product_id>')
class ResMenuItem(Resource):
    @api.doc("get specific product details", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found The Product"})
    @jwt_required()
    @authorization_check.restaurant_required()
    def get(self, product_id):
        """Get specific product details"""
        current_user = get_jwt()
        return RestaurantService.get_product(current_user['res_id'],product_id)

    
    @api.doc("update specific product", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found The Product"})
    @api.expect(product_update_data)
    @jwt_required()
    @authorization_check.restaurant_required()
    def put(self, product_id):
        """Update specific product """
        update_data = request.get_json()
        current_user = get_jwt()
        return RestaurantService.update_product(current_user['res_id'],product_id, update_data)
    
    @api.doc("delete specific product", responses={
    200: ("Success"),
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found The Product"})
    @jwt_required()
    @authorization_check.restaurant_required()
    def delete(self, product_id):
        """Delete specific product"""
        current_user = get_jwt()
        return RestaurantService.delete_product(current_user['res_id'],product_id)