nr_bile = 300
nr_iteratie = 0
nr_crt = 1
bile_verzi = 0


while nr_iteratie < nr_bile:
    nr_iteratie += 1
    if nr_crt % 2 == 0:
        bile_verzi += 1
        nr_crt += 3

    print(bile_verzi)