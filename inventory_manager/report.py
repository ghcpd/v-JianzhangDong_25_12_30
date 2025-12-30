import pandas as pd
from typing import Iterable


def export_report(products: Iterable[object], filename: str) -> None:
    """Export a list of product-like objects to an Excel file using pandas.

    Each product must expose `id`, `name`, `qty`, and `price` attributes.
    """
    rows = [
        {"id": p.id, "name": p.name, "qty": p.qty, "price": p.price}
        for p in products
    ]
    df = pd.DataFrame(rows)
    df.to_excel(filename, index=False)
