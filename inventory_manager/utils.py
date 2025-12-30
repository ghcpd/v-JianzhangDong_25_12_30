def calculateTotal(products):
    total_qty=0
    total_value=0
    for p in products:
        total_qty += p.qty
        total_value += p.qty*p.price
    return total_qty, total_value
