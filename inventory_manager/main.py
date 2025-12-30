from inventory_manager.database import InventoryDB
from inventory_manager.models import Product
from inventory_manager.utils import calculateTotal
from inventory_manager.report import export_report

def main():
    db=InventoryDB("inventory.db")
    db.create_table()
    products=[
        Product(1,"Apple",100,0.5),
        Product(2,"Banana",200,0.3),
        Product(3,"Orange",150,0.4)
    ]
    for p in products:
        db.add_product(p)
    all_products=db.get_all_products()
    total_qty,total_value=calculateTotal(all_products)
    print("Total quantity:",total_qty,"Total value:",total_value)
    export_report(all_products,"report.xlsx")

if __name__=="__main__":
    main()
