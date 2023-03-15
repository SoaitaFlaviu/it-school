def box_price(height, length, width, t=25, price=25):
    raw_price = height * length * width * price
    if t == 1:
        return raw_price
    if t == 2:
        return raw_price * 1.1
    if t == 3:
        return raw_price * 1.2


print(box_price(1, 2, 3, price=26, t=3))