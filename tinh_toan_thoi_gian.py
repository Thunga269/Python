
t = int(input())
a =[]
from datetime import datetime
for i in range(t):
    code = input()
    name = input()
    format = "%H:%M"
    time_in = datetime.strptime(input(), format)
    time_out= datetime.strptime(input(), format)
    time = str(time_out-time_in).split(":")
    minute = int(time[0])*60+int(time[1])
    a.append([code, name, time, minute])
a.sort(reverse=True, key = lambda x: x[3])
for i in a:
    print(i[0], i[1], "%s gio %s phut" % (int(i[2][0]), int(i[2][1])))