
def load_order_data(order_obj):
    from app.models.schemas import OrderSchema
    order_schema = OrderSchema()
    order_data = order_schema.dump(order_obj)
    return order_data