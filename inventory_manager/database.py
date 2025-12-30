import sqlite3
from inventory_manager.models import Product


class InventoryDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS products "
            "(id INTEGER PRIMARY KEY, name TEXT, qty INTEGER, price REAL)"
        )
        self.conn.commit()

    def add_product(self, product: Product):
        self.cur.execute(
            "INSERT INTO products (id, name, qty, price) VALUES (?, ?, ?, ?)",
            (product.id, product.name, product.qty, product.price)
        )
        self.conn.commit()

    def get_all_products(self):
        self.cur.execute("SELECT id, name, qty, price FROM products")
        rows = self.cur.fetchall()
        return [Product(*r) for r in rows]
