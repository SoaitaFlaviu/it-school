
import random
import time
from datetime import datetime


l1 = [random.randint(1, 99999) for u in range(1000000)]

start = time.time()
l1.sort()
stop = time.time()
print(f"Executia a durat {stop - start} s")

