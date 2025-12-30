from typing import Iterable, Tuple


def calculate_total(products: Iterable[object]) -> Tuple[int, float]:
    """Calculate total quantity and total value for an iterable of products.

    Expects each product to have `qty` and `price` attributes.
    """
    total_qty = 0
    total_value = 0.0

    for p in products:
        total_qty += p.qty
        total_value += p.qty * p.price

    return total_qty, total_value
