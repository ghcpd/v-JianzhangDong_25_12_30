"""Database helpers for inventory_manager."""
from typing import List

import sqlite3

from inventory_manager.models import Product


class InventoryDB:
    """Lightweight SQLite helper for product storage."""

    def __init__(self, db_file: str) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def create_table(self) -> None:
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS products "
            "(product_id INTEGER PRIMARY KEY, name TEXT, qty INTEGER, price REAL)"
        )
        self.conn.commit()

    def add_product(self, product: Product) -> None:
        self.cur.execute(
            "INSERT INTO products (product_id, name, qty, price) VALUES (?,?,?,?)",
            (product.product_id, product.name, product.qty, product.price),
        )
        self.conn.commit()

    def get_all_products(self) -> List[Product]:
        self.cur.execute("SELECT product_id, name, qty, price FROM products")
        rows = self.cur.fetchall()
        return [Product(*r) for r in rows]
