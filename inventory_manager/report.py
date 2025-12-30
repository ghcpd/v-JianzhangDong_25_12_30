import pandas as pd
from typing import Iterable

from inventory_manager.models import Product


def export_report(products: Iterable[Product], filename: str) -> None:
    """Export products to an Excel file."""
    df = pd.DataFrame(
        [
            {"id": p.id, "name": p.name, "qty": p.qty, "price": p.price}
            for p in products
        ]
    )
    df.to_excel(filename, index=False)
