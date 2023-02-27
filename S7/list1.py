user_id = [324, 4, 345, 534, 64, 4, 345]

#user_id.append(44) # Sa a

#user_id.insert(1, 55) # Sa adaugi un element 

print(user_id)

#print(user_id.index(4, 5))  #Sa gasesti un element in lista

#user_id.insert(user_id.index(345) + 1, 44)

#print(user_id)

index = -1

for i in range(user_id.count(345)):
    index = user_id.index(345, index + 1)
    user_id.insert(index + 1, 44)

print(user_id)

user_id_ro = tuple(user_id)

print(user_id_ro)