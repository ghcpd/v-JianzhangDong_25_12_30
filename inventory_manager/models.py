from dataclasses import dataclass


@dataclass
class Product:
    """Represents a product in inventory."""

    product_id: int
    name: str
    qty: int
    price: float

    def __str__(self) -> str:
        return f"Product({self.product_id}, {self.name!r}, {self.qty}, {self.price})"
