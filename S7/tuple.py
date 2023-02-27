countries = ("Romania", "Albania", "Ungaria")

print(countries)
print(type(countries))

print(countries[0]) #Accesez un element prin index 

#Doar functiile count si index pentru 'tuple'

countries_list = list(countries)

print(countries_list)

for i in enumerate(countries):
    print(i[0], i[1])             # Sau i, j print(i, j)

 