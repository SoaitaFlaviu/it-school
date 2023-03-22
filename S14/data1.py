from faker import Faker
fake = Faker("ro_RO")

for i in range(50):
    print(fake.name())