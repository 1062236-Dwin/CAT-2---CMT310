import uuid

class OrderProcessor:
    def place_order(self, cart):
        if not cart.items:
            raise ValueError("Cannot place an order with an empty cart")

        for product, quantity in cart.items.items():
            if product.stock < quantity:
                raise ValueError(f"Not enough stock for {product.name}")
        
        for product, quantity in cart.items.items():
            product.reduce_stock(quantity)

        return str(uuid.uuid4())  # Generates uniq order id and the import at the top helps thisnwork
