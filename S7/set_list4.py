list1 = [22, 34, 55, 10, 19]

list2 = [23, 34, 65, 55]

common = set(list1).intersection(set((list2))) #Face intersectia dintre doua seturi!
diff = set(list1).difference(set((list2))) # Numerele care se gasesc in prima lista si nu in prima 
diff1 = set(list2).difference(set((list1)))

print(common)
print(diff)
print(diff1)

set1 = set(list1)
set1.update(list2)

print(set1)

