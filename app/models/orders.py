from enum import Enum
from app import db
from datetime import datetime

class OrderStatus(Enum):
    NEW = 1
    PREPARING = 2
    ONTHEWAY = 3
    DELIVERED = 4
    RESTAURANT_CANCELLED = 5
    CUSTOMER_CANCELLED = 6
    

class OrdersTable(db.Model):
    """
    Orders table
    """
    __tablename__="orders"
    order_id = db.Column(db.Integer, primary_key=True)
    res_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_ids = db.Column(db.String(80), nullable=False)
    quantities = db.Column(db.String(80), nullable=False)
    order_date = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    order_status = db.Column(db.String(80),default=OrderStatus.NEW.name ,nullable=False)
    

    def __repr__(self):
        return '<OrdersTable {}>'.format(self.name)
