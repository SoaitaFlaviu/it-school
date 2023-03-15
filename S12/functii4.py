def zero_one(lst):
    lst_in = lst[:] # creaza o lista goala noua
    lst_in[1] = 1
    return lst_in 

matrix = [
    [0, 3, 4, 4],
    [2, 34, 24, 43],
]    

print(matrix)
zero_one(matrix) # pass by reference 
print(matrix)

