students_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}

#Cum extragem lista keu

lista_chei = students_grades.keys() #Daca adaugam un key nou , se adauga automat

print(type(lista_chei))

print(lista_chei)

for name in lista_chei:
    print(name)

print("-" * 30)

    #Extragere lista valori 

for value in students_grades.values():
    print(value)

print("-" * 30)

    #Cum extragem perechi key/valoare

valori = students_grades.items()

print(valori)

print(list(valori)[0])

for v in valori:
    print(v) #print(v[0]) doar numele
             #name, grade = v print
print("-" * 30)
for k, v in students_grades.items():
    print(k, v)
