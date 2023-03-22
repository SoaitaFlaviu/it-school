# all - true daca toate valorile din lista evalueaza True

print(all([True, True]))

# any - true daca oricare element este True 

print(any([True, False, False]))

# map
init_lst = [4, 56, 7, 5, 45]
new_lst = map(lambda x: x ** 2, init_lst)
new_lst1 = [x ** 2 for x in init_lst]
print(new_lst)

#enumerate

print(enumerate(init_lst))

for i in enumerate(init_lst):
    print(f"Index {i[0]} ... valoare {i[1]}")


# divmod

ambele = divmod(10, 3)

print(ambele)


cat, rest = divmod(10, 3)
print(f"Catul = {cat} si restul = {rest}")

# zip 

names = ["Alex", "Elena", "Victor"]
id = ["23323", "353535", "351234"]

print(zip(names, id))

zp = (zip(names, id))

for i in zp:
    print(i)


