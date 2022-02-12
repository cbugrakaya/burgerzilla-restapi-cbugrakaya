from app import db

# TODO : Class enum yapısına bak


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
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    order_status = db.Column(db.String(80), nullable=False)
    

    def __repr__(self):
        return '<OrdersTable {}>'.format(self.name)
