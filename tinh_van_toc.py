t = int(input())
a={}
for _ in range(t):
    ten = input()
    donVi = input()
    thoiGian = [int(x) for x in input().split(':')]
    tim = ((thoiGian[0]-6)*60 + thoiGian[1])
    # print(tim)
    vanToc = 120 / ((thoiGian[0]-6) + thoiGian[1]/60)
    # print(vanToc)
    ma = ''
    for i in donVi.split():
        ma += i[0]
    for i in ten.split():
        ma += i[0]
    a[ma] = [ten, donVi, (vanToc)]
a = sorted(a.items(), key=lambda x: -x[1][2])
# print(*a)
for i in a:
    print(i[0], i[1][0], i[1][1], round(i[1][2]), 'Km/h')
