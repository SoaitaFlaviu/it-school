from datetime import datetime



now = datetime.now()

ev1 = datetime(1993, 8, 29)

print(f'I was born on{ev1.strftime("%A")}')

