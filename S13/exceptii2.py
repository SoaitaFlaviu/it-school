
def circle_area(radius):
    """Calculate circle area. Radius has to be a positive 
    
    Args:
        - radius (float): Circle radius.
    
    Raises:
        - ValueError: If radius is less than 0.
    """
    if radius < 0:
        raise ValueError("Valoare nu poate fii negativa")
    
    return 3.14 * radius ** 2


number = float(input("Raza cerc: "))


try:
    print(circle_area(number))
except ValueError as err:
    print(f"[ERROR] {err}")

