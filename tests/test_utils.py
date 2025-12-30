from inventory_manager.utils import calculate_total
from inventory_manager.models import Product


def test_calculate_total_empty():
    assert calculate_total([]) == (0, 0.0)


def test_calculate_total_values():
    products = [Product(1, "A", 2, 1.5), Product(2, "B", 3, 2.0)]
    qty, value = calculate_total(products)
    assert qty == 5
    assert value == 2 * 1.5 + 3 * 2.0
