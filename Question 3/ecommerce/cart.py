class ShoppingCart:
    def __init__(self):
        self.items = {}  # product -> quantity

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if product.stock < quantity:
            raise ValueError("Insufficient stock")

        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())
