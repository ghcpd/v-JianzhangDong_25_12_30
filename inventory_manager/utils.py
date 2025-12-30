def calculate_total(products):
    """Return total quantity and total value for an iterable of products.

    Args:
        products: Iterable of product-like objects with ``qty`` and ``price``.

    Returns:
        Tuple[int, float]: (total_qty, total_value)
    """
    total_qty = sum(p.qty for p in products)
    total_value = sum(p.qty * p.price for p in products)
    return total_qty, total_value
