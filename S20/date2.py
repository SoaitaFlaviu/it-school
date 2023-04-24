import time

now = time.time()

now_tm = (time.gmtime(now))

print(now_tm.tm_year)

print(f"Suntem in ziua:{now_tm.tm_yday} Luna:{now_tm.tm_mday}")