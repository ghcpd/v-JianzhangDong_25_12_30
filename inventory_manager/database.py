import sqlite3
from typing import List

from inventory_manager.models import Product


class InventoryDB:
    """Simple wrapper around SQLite for product storage."""

    def __init__(self, db_file: str) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def create_table(self) -> None:
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS products ("
            "id INTEGER PRIMARY KEY, name TEXT, qty INTEGER, price REAL)"
        )
        self.conn.commit()

    def add_product(self, product: Product) -> None:
        self.cur.execute(
            "INSERT OR REPLACE INTO products ("
            "id, name, qty, price) VALUES (?, ?, ?, ?)",
            (product.id, product.name, product.qty, product.price),
        )
        self.conn.commit()

    def get_all_products(self) -> List[Product]:
        self.cur.execute("SELECT id, name, qty, price FROM products")
        rows = self.cur.fetchall()
        return [Product(*r) for r in rows]

    def close(self) -> None:
        self.conn.close()
