class Car:
    """Representation of a virtual car."""

    def __init__(self): # constructor
        self.__cmc = 1600
        self.__doors = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 0
        self.__passengers = []
        self.__engine_running = False
    
    def get_gas_percentage(self):
        """Get current gas level in tank."""
        return self.__gas_in_tank / self.__tank_capacity * 100
    
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def drive(self, km):
        """1. verifica daca motorul functioneaza, daca nu exceptie
        2. verifici daca poti parcurge km, daca nu ai combustibil ridici exceptie
        3. daca ai combustibil sa parcurgi km, trebuie consumat conbustibilul 
    - consuml per km se calculeaza ca fiind __cmc / 1000
        """
        pass

    def refill(self, litters):
        if litters > self.__tank_capacity - self.__gas_in_tank:
            raise ValueError("Overflow")
        self.__gas_in_tank = litters
    
    def get_doors(self):
        return self.__doors

class Person:

    def __init__(self):  # constructor
        self.height = 187 # cm
        self.weight = 0


vlad = Person()
maria = Person()

vw = Car()
ford = Car()


# print(f"CMC VW: {vw.__cmc}")
# print(f"CMC Ford: {ford.__cmc}")

# vw.__cmc = 3000

# print(f"CMC VW: {vw.__cmc}")
# print(f"CMC Ford: {ford.__cmc}")


print(vw.get_doors())
print(f"Combustibil ramas {vw.get_gas_percentage()} %")
vw.refill(12)
print(f"Combustibil ramas {vw.get_gas_percentage():.2f} %")