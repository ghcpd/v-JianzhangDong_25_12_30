import pandas as pd
from typing import Iterable


def export_report(products: Iterable, filename: str) -> None:
    """Export products to an Excel file.

    The exported columns are: product_id, name, qty, price.
    """
    df = pd.DataFrame(
        [
            {
                "product_id": p.product_id,
                "name": p.name,
                "qty": p.qty,
                "price": p.price,
            }
            for p in products
        ]
    )
    df.to_excel(filename, index=False)

