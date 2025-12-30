from inventory_manager.database import InventoryDB
from inventory_manager.models import Product
from inventory_manager.utils import calculate_total
from inventory_manager.report import export_report
from inventory_manager.config import DB_FILE, REPORT_FILE


def main() -> None:
    """Populate the database with sample products and export a report."""
    db = InventoryDB(DB_FILE)
    db.create_table()

    products = [
        Product(1, "Apple", 100, 0.5),
        Product(2, "Banana", 200, 0.3),
        Product(3, "Orange", 150, 0.4),
    ]

    for product in products:
        db.add_product(product)

    all_products = db.get_all_products()
    total_qty, total_value = calculate_total(all_products)
    print(f"Total quantity: {total_qty}  Total value: {total_value:.2f}")

    export_report(all_products, REPORT_FILE)


if __name__ == "__main__":
    main()
