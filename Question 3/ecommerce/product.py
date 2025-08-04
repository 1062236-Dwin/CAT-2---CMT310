class Product:
    def __init__(self, name, price, stock):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock.")
        self.stock -= quantity

    def increase_stock(self, quantity):
        self.stock += quantity