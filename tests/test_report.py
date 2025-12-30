import os
from inventory_manager.report import export_report
from inventory_manager.models import Product


def test_export_report(tmp_path):
    out = tmp_path / "out.xlsx"
    products = [Product(1, "A", 1, 1.0)]
    export_report(products, str(out))
    assert out.exists()
    assert out.stat().st_size > 0
