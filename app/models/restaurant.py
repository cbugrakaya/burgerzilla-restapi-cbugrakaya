from app import db


class Restaurant(db.Model):
    __tablename__="restaurant"
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(80), nullable=False)
    owner_name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)
