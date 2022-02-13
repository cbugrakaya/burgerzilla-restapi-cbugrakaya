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


class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('order_id','res_id', 'user_id', 'product_ids', 'quantities', 'order_date', 'order_status')

    
class ProductSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'res_id', 'product_name', 'price_tl', 'description', 'image_url')