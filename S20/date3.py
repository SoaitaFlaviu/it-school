import time

event_time = "12 April 2023 16:48:53"

ev_tm = time.strptime(event_time, "%d %B %Y %H:%M:%S")

print(ev_tm)

ev1 = "20-20-2023 10:11"
ev2 = "20-02-2023 12:45"

ev_bt = time.strptime(ev1, "%d-%m-%Y %H:%M")
ev_bt1 = time.strptime(ev2, "%d-%m-%Y %H:%M")

det_bt = ev_bt.tm_min - ev_bt1.tm_min
delta_h = (ev_bt.tm_hour - ev1_tm.tm_hour)