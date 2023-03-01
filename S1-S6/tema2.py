# Exercitiul 1 
# Scrie un program care citeste de la tastatura un numar natural si afiseaza "Par" daca numarul este par sau "Impar" daca numarul este impar.

valoare = int(input("Introduceti un numar:"))

if valoare % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")

# Exercitiul 2
# Scrie un program care citeste de la tastatura un numar  natural, reprezentand raza unui cerc, si afiseaza perimetrul
# cercului insotit de mesajul "Perimetru cercului = <valoare>".Daca numarul citit este mai mare decat 100 se va calcula si aria
# cercului. Aceasta se va afisa insotita de mesajul "Aria cercului = <valoare>".

pi = 3.14

val = int(input("Raza cercului este:"))

pcerc = 2 * pi * val

arcerc = pi * val ** 2

if val <= 100: 
    print("Perimetrul cercului este:" + str(pcerc))
elif val > 100:
    print("Perimetrul cercului este:" + str(pcerc))
    print("Aria cercului este:" + str(arcerc))

# Exercitiul 3
#Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b sa se diferenta suma lor.
# Daca a == b sa se afiseze a la puterea b
# Altfel sa se afiseze suma lor.


a = int(input("Introduceti primul numar:"))
b = int(input("Introduceti al doilea numar:"))

if a > b:
    print(a-b)
elif a == b:
    print(a**b)
else:
    print(a+b)

#Exercitiul 4 
#Scrie un program care citeste de la tastatura doua numere, si calculeaza a / b daca a > b sau b / a daca a <= b. Afiseaza rezultatul.

a = int(input("Introduceti primul numar:"))
b = int(input("Introduceti al doilea numar:"))

if a > b:
    print(a / b)
elif a <= b:
    print(b / a)

#Exercitiul 5
#  Scrie un program care citeste de la tastatura un numar natural pozitiv din 3 cifre. Daca numarul introdus nu are 3 cifre sau este un numar negativ se afiseaza: "Eroare".
# Daca ultima cifra din numarul introdus este mai mare sau egala cu 5,
# se va afisa suma dintre numarul introdus si ultima sa cifra, altfel 
# se va afisa diferenta dintre numarul introdus si ultima sa cifra.

nrcrt = int(input("Introduceti un numar format din trei cifre:" )) 

if nrcrt < 100 or nrcrt > 999:
    print("Eroare")
if nrcrt % 10 >= 5:
    print(nrcrt+(nrcrt%10))
else:
    print(nrcrt-(nrcrt%10))

#Exercitiul 6
#  Scrie un program care afiseaza urmatoarea 
# sctructura, unde n = 6, folosind instructiunea while:
#a = int(input("Introduceti un numar pana la 10: "))

n = int(input("Introducet un numar"))

c = 1

while n <= 10:
    print("*" * c)
    c = c + 1

