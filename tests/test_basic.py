import os
import tempfile

from inventory_manager.database import InventoryDB
from inventory_manager.models import Product
from inventory_manager.utils import calculate_total
from inventory_manager.report import export_report


def test_product_dataclass():
    p = Product(1, "widget", 3, 2.5)
    assert p.product_id == 1
    assert p.name == "widget"
    assert str(p).startswith("Product(")


def test_calculate_total():
    products = [Product(1, "a", 2, 1.5), Product(2, "b", 3, 2.0)]
    qty, value = calculate_total(products)
    assert qty == 5
    assert value == 2 * 1.5 + 3 * 2.0


def test_inventory_db_roundtrip(tmp_path):
    db = InventoryDB(":memory:")
    db.create_table()
    p = Product(10, "dbtest", 1, 0.99)
    db.add_product(p)
    rows = db.get_all_products()
    assert any(r.product_id == 10 and r.name == "dbtest" for r in rows)


def test_export_report_creates_file(tmp_path):
    products = [Product(1, "x", 1, 1.0)]
    out = tmp_path / "report.xlsx"
    export_report(products, str(out))
    assert out.exists()
    assert out.stat().st_size > 0
