#Exercitiul 1

dict1 = {
    'Alex': 25,
    'Maria': 30,
    'Andrei': 21,
}

print(dict1)

for k, v in dict1.items():
    print(k, v)

print("-" * 30)

#Exercitiul 2


dict2 = {
    'Alex': [3, 5, 6],
    'Maria': [5, 7 ,1],
    'Andrei': [2, 5, 8],
}

for k, v in dict2.items():   #Iteratie la un dictionar 
    media = sum(v) / len(v)

    print(k, media)

print("-" * 30)

#Exercitiul 3 

dict3 = {
    'Andrei': 12,
    'Ionut': 19,
    'Marian': 22,
}

dict4 = dict3.keys()

print(dict4)

print(sorted(dict4, reverse = True))

print("-" * 30)

