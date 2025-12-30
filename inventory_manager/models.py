class Product:
    """Simple product model for inventory entries."""

    def __init__(self, product_id: int, name: str, qty: int, price: float) -> None:
        self.id = product_id
        self.name = name
        self.qty = qty
        self.price = price

    def __str__(self) -> str:
        return f"Product({self.id}, {self.name}, {self.qty}, {self.price})"
