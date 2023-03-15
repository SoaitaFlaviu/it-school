def box_price(height, length, width, t=25, price=25, **kwargs):
    raw_price = height * length * width * price
    if t == 1:
        return raw_price
    if t == 2:
        return raw_price *kwargs.get("cq2", 1.1)
    if t == 3:
        return raw_price * kwargs.get("cq3", 1.1)
    

def demo(**kwargs):              #kwargs este dictionar
    print(kwargs)

demo(a=3, b=3, alex=32, new="test")
