from autos import Car
from user import Person

ford = Car()

print(ford.get_gas_percentage())
print(ford.get_consumption())
ford.start_engine()
ford.refill(45)
ford.drive(1)

p1 = Person()
p2 = Person()

ford.add_person(p1)
ford.add_person(p2)
print(ford.get_consumption())