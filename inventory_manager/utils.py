from typing import Iterable, Tuple


def calculate_total(products: Iterable[object]) -> Tuple[int, float]:
    """Calculate total quantity and total value for a sequence of products."""
    total_qty = sum(p.qty for p in products)
    total_value = sum(p.qty * p.price for p in products)
    return total_qty, total_value
