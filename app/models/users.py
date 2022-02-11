from app import db 
from werkzeug.security import check_password_hash,generate_password_hash



# class Roles(db.Model):
#     __tablename__ = 'role'
#     id = db.Column(db.Integer, primary_key=True)
#     role_int = db.Column(db.Integer)

#     role_description = db.Column(db.String(80))
    
class Users(db.Model):
    """
    User table"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role_type = db.Column(db.String(80), nullable=False)
   
    userdataset = db.relationship("Restaurant", backref="users", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Users {self.username}>"
