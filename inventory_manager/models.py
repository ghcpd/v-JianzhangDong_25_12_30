class Product:
    def __init__(self, id, name, qty, price):
        self.id = id
        self.name = name
        self.qty = qty
        self.price = price

    def __str__(self):
        return f"Product({self.id}, {self.name}, {self.qty}, {self.price})"
