import pandas as pd


def export_report(products, filename):
    df = pd.DataFrame([
        {'id': p.id, 'name': p.name, 'qty': p.qty, 'price': p.price}
        for p in products
    ])
    df.to_excel(filename, index=False)
