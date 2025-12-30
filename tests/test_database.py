import os
import tempfile
from inventory_manager.database import InventoryDB
from inventory_manager.models import Product


def test_add_and_get_products(tmp_path):
    db_file = tmp_path / "test.db"
    with InventoryDB(str(db_file)) as db:
        db.create_table()
        db.add_product(Product(1, "X", 10, 1.0))
        rows = db.get_all_products()
        assert len(rows) == 1
        assert rows[0].name == "X"
