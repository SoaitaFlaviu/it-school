
user_ids = [324, 345, 536, 64, 4]

# for i in range(len(user_ids)):
#     print("Index:", i, "  Valoare:", user_ids[i])

for i in enumerate(user_ids):
    print("Index:", i[0], "  Valoare:", i[1])

counter = 0 

for i in range(0, 1000, 5):
    counter += i

print(counter)

