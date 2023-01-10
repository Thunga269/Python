def time(start, end):
    return -(start[0]*60+start[1]-end[0]*60-end[1]) # thời gian đo được

a = {}
t = int(input())

for i in range(t):
    ten = input()
    start = [int(x) for x in input().split(':')]
    end = [int(x) for x in input().split(':')]
    luongMua = int(input())
    if ten not in a:
        a[ten] = (time(start, end), luongMua) # a[ten][0]: thời gian; a[ten][1]: lượng mưa
    else:   
        a[ten] = (a[ten][0] + time(start, end), a[ten][1] + luongMua)

p = 1
# print(a)
for i in a:
    k = 'T0'+ str(p)
    print(k, i, "{:.2f}".format(a[i][1] * 60 / a[i][0])) 
    p+=1
#     print('T{:02d}'.format(p), i, "{:.2f}".format(a[i][1] * 60 / a[i][0]))