def range_product(start, stop):
    """Calculate the product for numbers between start and stop."""
    prod = 1
    for i in range(start, stop):
        prod *= i
        # prod = prod * i
    return prod

start_in = 1
stop_in = 10

print(f"Produsul numerelor din intervalul {start_in} si {stop_in} este {range_product(stop_in, stop_in)}")
