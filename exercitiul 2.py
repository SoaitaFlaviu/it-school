from random import randint

ran_nr = randint(1, 99)

print ("Incepe Jocul")

a = int(input("Introduceti un numar intre 1 si 99:"))

while a != ran_nr:
    if a < ran_nr:
        print("Mai mare")
    elif a > ran_nr:
        print("Mai mic")
    a = int(input("Introduceti un numar intre 1 si 99:"))
        
print("Felicitari ai ghicit")
print("Numarul a fost ", ran_nr)
