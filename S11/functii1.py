def is_even(number):
    if number %  2 == 0:
        return  True
    else:
        return False
    
#main


a = 4

a_even = is_even(a)

print(f"Variabila a este numar par ? {a_even}")