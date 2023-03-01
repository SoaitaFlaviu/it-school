students_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}

print(students_grades["Ana"])

nota = print(students_grades.get("Ana")) # Nu da eroare daca nu exista key-ul respectiv

if nota is not None:
    print(nota)
else:
    print("Studentul nu exista")

