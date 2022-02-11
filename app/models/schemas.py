from app import ma
from .users import Users  

class UsersSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('fullname', 'email', 'role_type')

class RestaurantSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'restaurant_name', 'owner_id')


