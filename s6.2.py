temp = [33, 22, 34, 0, 21, 22, 0]
to_remove = 22

print(temp)

print(to_remove, "apare de ", temp.count(to_remove), "ori")

while to_remove in temp:
    temp.remove(to_remove)

print(temp)

if 0 in temp:
    print("S-a produs inghet")
    if temp.count(0) > 1:
        print("S-a produs inghet de mai multe ori")

temp1 = temp.copy()
temp1.reverse()

print(temp)
print(temp1)

print("Temperatura maxima", max(temp))
print("Temperatura minima", min(temp))