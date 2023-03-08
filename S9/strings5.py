user_code = "44563-Test-0001"

#print(user_code.find('-'))

prev = 0

while prev != -1:
    prev = user_code.find("-", prev + 1)
    print(prev)

