from json import load
from flask import current_app
from app import db

from enum import Enum
from app.utils import message, err_resp, internal_err_resp
from app.models.users import Users
from app.models.restaurant import Restaurant
from app.models.orders import OrdersTable, OrderStatus
from app.models.products import ProductsTable

class RestaurantService:

    """ResOrder Service BEGIN""" 
    @staticmethod
    def get_order(res_id,order_id):
        """
        get specific order
        """
        if not (order := OrdersTable.query.filter_by(order_id=order_id,res_id=res_id).first()):
            return err_resp(msg="Not Found Order", code=404, reason="order_not_found")
        from .utils import load_order_data
        try:
            order_data = load_order_data(order)
            resp = message(True,"Order Found")
            resp['order_data'] = order_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
        
    @staticmethod
    def update_order(res_id,order_id, update_data):
        """
        Update specific order status
        """
        if not (order := OrdersTable.query.filter_by(order_id=order_id,res_id=res_id).first()):
            return err_resp(msg="Not Found Order", code=404, reason="order_not_found")
        try:
            # if status between 1 and 5
            if not(update_data['status'] in range(1,6)):
                return err_resp(msg="Invalid status for order(1,5)", code=402, reason="invalid_status")
            if order.order_status == OrderStatus.RESTAURANT_CANCELLED.name or order.order_status == OrderStatus.CUSTOMER_CANCELLED.name:
                return err_resp(msg="Order Cancelled",code=403,reason="order_cancelled")
            order.order_status = OrderStatus(update_data['status']).name
            db.session.commit()
            resp = message(True,"Order Status Updated")
            return resp,200
        except Exception as e:
                    current_app.logger.error(e)
                    return internal_err_resp()     

    @staticmethod
    def cancel_order(res_id,order_id):
        """
        Cancel specific order
        """
        if not (order := OrdersTable.query.filter_by(order_id=order_id,res_id=res_id).first()):
            return err_resp(msg="Not Found Order", code=404, reason="order_not_found")
        try:
            order.order_status = OrderStatus.RESTAURANT_CANCELLED.name
            db.session.commit()
            resp = message(True,"Order Canceled")
            return resp,200
        except Exception as e:
                    current_app.logger.error(e)
                    return internal_err_resp()
    """ResOrder Service END"""

    """ResOrderList Service BEGIN"""
    @staticmethod
    def get_all_orders(res_id):
        """
        Get all orders
        """
        if not (orders := OrdersTable.query.filter_by(res_id=res_id).all()):
            return err_resp(msg="Not Found Any Order", code=404, reason="order_not_found")
        from .utils import load_order_data
        try:
            orders_data = [load_order_data(order) for order in orders]
            resp = message(True,"All Orders Found")
            resp['orders'] = orders_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
    """ResOrderList Service END"""

    """ResMenu Service BEGIN"""
    @staticmethod
    def get_menu(res_id):
        """
        Get menu
        """
        if not (menus := ProductsTable.query.filter_by(res_id=res_id).all()):
            return err_resp(msg="Not Found Menu", code=404, reason="menu_not_found")
        from .utils import load_product_data
        try:
            menu_data = [load_product_data(menu) for menu in menus]
            resp = message(True,"Menu Found")
            resp['menu'] = menu_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    # FIX : This is not necessary or confusig
    # @staticmethod
    # def update_menu(res_id,product_id, update_data):
    #     """
    #     Update menu
    #     """
    #     if not (menu := ProductsTable.query.filter_by(id=product_id,res_id=res_id)):
    #         return err_resp(msg="Not Found Menu", code=404, reason="menu_not_found")
    #     try:
    #         menu.product_name = update_data['product_name']
    #         menu.product_price = update_data['product_price']
    #         menu.product_description = update_data['product_description']
    #         menu.product_image_url = update_data['product_image_url']
    #         db.session.commit()
    #         resp = message(True,"Menu Updated")
    #         return resp,200
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return internal_err_resp()

    @staticmethod
    def add_product(res_id,product_data):
        """
        Add product
        """
        if not (restaurant := Restaurant.query.filter_by(id=res_id).first()):
            return err_resp(msg="Not Found Restaurant", code=404, reason="restaurant_not_found")
        try:
            product = ProductsTable(
                res_id=res_id,
                product_name=product_data['product_name'],
                price_tl=product_data['product_price'],
                description=product_data['product_description'],
                image_url=product_data['product_image_url']
            )
            db.session.add(product)
            db.session.commit()
            resp = message(True,"Product Added")
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
    """ResMenu Service END"""
    


    """ResMenuProductLıst Service BEGIN"""
    @staticmethod
    def get_all_products(res_id):
        """
        Get all products
        """
        if not (products := ProductsTable.query.filter_by(res_id=res_id).all()):
            return err_resp(msg="Not Found Any Product", code=404, reason="product_not_found")
        from .utils import load_product_data
        try:
            products_data = [load_product_data(product) for product in products]
            resp = message(True,"All Products Found")
            resp['products'] = products_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    """ResMenuProductLıst Service END"""   


    """ResMenuItem Services BEGIN"""
    @staticmethod
    def get_product(res_id,product_id):
        """
        get specific product details
        """
        if not (product := ProductsTable.query.filter_by(id=product_id,res_id=res_id).first()):
            return err_resp(msg="Not Found Product", code=404, reason="product_not_found")
        from .utils import load_product_data
        try:
            product_data = load_product_data(product)
            resp = message(True,"Product Found")
            resp['product_data'] = product_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_product(res_id,product_id, update_data):
        """
        Update specific product 
        """
        if not (product := ProductsTable.query.filter_by(id=product_id,res_id=res_id).first()):
            return err_resp(msg="Not Found Product", code=404, reason="product_not_found")
        try:
            if 'product_name' in update_data:
                product.product_name = update_data['product_name']
            if 'product_price' in update_data:
                product.price_tl = update_data['product_price']
            if 'product_description' in update_data:
                product.description = update_data['product_description']
            if 'product_image_url' in update_data:
                product.image_url = update_data['product_image_url']
        
            db.session.commit()
            resp = message(True,"Product Updated")
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
    
    @staticmethod
    def delete_product(res_id,product_id):
        """
        Delete specific product
        """
        if not (product := ProductsTable.query.filter_by(id=product_id,res_id=res_id).first()):
            return err_resp(msg="Not Found Product", code=404, reason="product_not_found")
        try:
            db.session.delete(product)
            db.session.commit()
            resp = message(True,"Product Deleted")
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
    """ResMenuItem Services END"""