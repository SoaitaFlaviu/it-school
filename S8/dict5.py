students_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}

valori = students_grades.items()

print(sorted(valori))

#Sortare dupa cheie 

for k, v in sorted(students_grades.items()):
    print(k, v)

print("-" * 30)

#Sortare dupa valori

def extract(x):
    return x[1]

for k, v in sorted(students_grades.items(), key =extract):
    print(k, v)

    