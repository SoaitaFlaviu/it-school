user_info = {
    "first_name": "mihai",
    "last_name": "dinu",
    "adress": "Bucharest",
    "country": "Romania"
}

print("Nume: {} Prenume: {} Country: {}".format(
    user_info["last_name"], user_info["first_name"], user_info["country"]))

USER_TEMPLATE = "Nume: {} Prenume: {} Country: {}"

print(USER_TEMPLATE.format(
    user_info["last_name"], user_info["first_name"], user_info["country"]))

print(USER_TEMPLATE.format("IONUT", "mocanu", "ro"))

# Preia valorile din dictionar
USER_TEMPLATE = "Nume: {0} Prenume: {1} Country: {2}"

#Exercitul 2 

auto ={
    "marca": "Audi",
    "model": "A4",
    "usi": 4
}

user_car = "Detin o masina marca {}, model {} si are {} usi."

print(user_car.format(auto["marca"], auto["model"], auto["usi"]))

