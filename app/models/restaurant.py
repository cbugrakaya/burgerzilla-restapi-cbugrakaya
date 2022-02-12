from app import db


class Restaurant(db.Model):
    """
    Restaurant table
    """
    __tablename__="restaurant"
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(80), nullable=False)
    owner_name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    resdataset = db.relationship("ProductsTable", backref="restaurant", lazy="dynamic")
    orddataset = db.relationship("OrdersTable", backref="restaurant", lazy="dynamic")

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)
