dict1 = {
    "key1": 1,
    "key2": {
        "key1": 1,
        "key2": ["elem1", "elem2"]
    }
}

print(dict1)

lista_dict = dict1["key2"]

print(lista_dict)

print(dict1["key2"]["key2"][1]) #

dict1["key1"] = 2

print(dict1["key1"]) #Schimbare un element din dictionar

dict1["key3"] = set()

print(dict1)

del dict1["key2"]

print(dict1)

