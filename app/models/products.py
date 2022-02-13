from app import db


class ProductsTable(db.Model):
    """
    Product table
    """
    __tablename__="product"
    id = db.Column(db.Integer, primary_key=True)
    res_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    product_name = db.Column(db.String(80), nullable=False)
    price_tl = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return '<Product {}>'.format(self.name)
