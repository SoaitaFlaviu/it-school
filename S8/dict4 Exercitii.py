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


 #Exercitiul 4

dict4 = {
   'Alex' : 35,
   'Andrei' : 44,
   'Rares' : 23,
 }

dict4['Luca'] = '65'

print(dict4)

print("-" * 30)

#Exercitiul 5

dict5 = {
    'Alex' : 'Str. Oglinzilor',
   'Andrei' : 'Str. Uranus',
   'Rares' : 'Str. Albac',
}

print(dict5)

print("-" * 30)

dict5['Andrei'] = 'Str.Luces'

print(dict5)

print("-" * 30)

#Exercitiul 6

dict6 = {
    'Alex' : 35,
   'Andrei' : 44,
   'Rares' : 23,
}

del dict6['Rares']

print(dict6)

print("-" * 30)

#Exercitiul 7


