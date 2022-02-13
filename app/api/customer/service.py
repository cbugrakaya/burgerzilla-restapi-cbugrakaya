from json import load
from flask import current_app
from app import db

from app.utils import message, err_resp, internal_err_resp
from app.models.users import Users
from app.models.restaurant import Restaurant
from app.models.orders import OrdersTable, OrderStatus
from app.models.products import ProductsTable


class CustomerService:
    @staticmethod
    def get_order(current_user,order_id):
        """
        get specific order
        """

        if not (order := OrdersTable.query.filter_by(order_id=order_id,user_id=current_user).first()):
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
    def update_order(current_user,order_id, update_data):
        """
        Update specific order
        """

        if not (order := OrdersTable.query.filter_by(order_id=order_id,user_id=current_user).first()):
            return err_resp(msg="Not Found Order",code=404,reason="order_not_found")
        if order.order_status == OrderStatus.RESTAURANT_CANCELLED.name or order.order_status == OrderStatus.CUSTOMER_CANCELLED.name:
            return err_resp(msg="Order Cancelled",code=403,reason="order_cancelled")
        try:
            order.quantities = update_data['quantities']
            db.session.commit()
            resp = message(True,"Order Updated")
            return resp,200
        except Exception as e:
                    current_app.logger.error(e)
                    return internal_err_resp()            
    

    @staticmethod
    def cancel_order(current_user,order_id):
        """
        Cancel specific order
        """

        if not (order := OrdersTable.query.filter_by(order_id=order_id,user_id=current_user).first()):
            return err_resp(msg="Not Found Order", code=404, reason="order_not_found")
        if order.order_status == OrderStatus.RESTAURANT_CANCELLED.name or order.order_status == OrderStatus.CUSTOMER_CANCELLED.name:
                return err_resp(msg="Order Already Cancelled",code=402,reason="order_already_cancelled")
        try:
            order.order_status = OrderStatus.CUSTOMER_CANCELLED.name
            db.session.commit()
            resp = message(True,"Order Canceled")
            return resp,200
        except Exception as e:
                    current_app.logger.error(e)
                    return internal_err_resp()


    @staticmethod
    def get_all_orders(current_user):
        """
        Get all orders
        """
        if not (orders := OrdersTable.query.filter_by(user_id=current_user).all()):
            return err_resp(msg="Not Found Order",code=404, reason="order_not_found")
        from .utils import load_order_data
        try:
            orders_data = [load_order_data(order) for order in orders]
            resp = message(True,"Order Found")
            resp['order_data'] = orders_data
            return resp,200
        except Exception as e:
                    current_app.logger.error(e)
                    return internal_err_resp()


    @staticmethod
    def create_order(current_user,restaurant_id, new_order_data):
        """
        Create new order
        """
        product_ids = new_order_data['product_ids']
        quantities = new_order_data["quantities"]
        if not (restaurant := Restaurant.query.filter_by(id=restaurant_id).first()):
            return err_resp(msg="Not Found Restaurant", code=404, reason="restaurant_not_found")

        if not (products := ProductsTable.query.filter_by(id=product_ids).first()):
            return err_resp(msg="Not Found Product In This Restaurant", code=405, reason="product_not_found_in_restaurant")
    
        try:
            order = OrdersTable(user_id=current_user,
                                res_id=restaurant_id,
                                product_ids=product_ids, 
                                quantities=quantities)
            db.session.add(order)
            db.session.commit()
            resp = message(True,"Order Created")
            return resp,200
        except Exception as e:
                    current_app.logger.error(e)
                    return internal_err_resp()