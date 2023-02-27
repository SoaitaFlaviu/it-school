# list sliceing

temperaturi = [91, 32, 31, 87, 34, 36, 13, 0, 11, 88, 22, 56, 44, 9, 76, 66, -3]

#print(len(temperaturi))

new_temp = []

for i in range(10):
    new_temp.append(temperaturi[i])

#print(sorted(new_temp))


new_tempp = temperaturi[2:10] # Daca nu scrie nimic e o copie a listei

print(len(new_temp))

print(new_temp)

