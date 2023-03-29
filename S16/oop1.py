from autos import Car


ford = Car()

print(ford.get_gas_percentage())
print(ford.get_consumption())
ford.start_engine()
ford.refill(16)
ford.drive(250)