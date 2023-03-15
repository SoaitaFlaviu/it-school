def product(a, b, *args):
    """Calculate the product of a and b."""
    p = a * b
    for i in args:
        p *= i
        return p

def n_product(*args):
    p = 1
    for i in args:
        p *= i
    return p

print(n_product(1))
print(n_product(1, 2))
print(n_product(1, 2, 3))
print(n_product(1, 2, 3, 4))
