
# Functia set elimina duplicatele 

colors = {"Red", "Brown", "Blue", "White"}

#print(colors)
#print(type(colors))

#colors1 = {} / nu e set gol , este dictionar 

for i in colors:
    print(i)

colors.add("black")

#colors.clear() sterge elementele

colors.remove("White")

#colors.pop() elimina un element total random


print(colors)