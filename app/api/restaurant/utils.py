
def load_order_data(order_obj):
    from app.models.schemas import OrderSchema
    order_schema = OrderSchema()
    order_data = order_schema.dump(order_obj)
    return order_data

def load_product_data(product_obj):
    from app.models.schemas import ProductSchema
    product_schema = ProductSchema()
    product_data = product_schema.dump(product_obj)
    return product_data