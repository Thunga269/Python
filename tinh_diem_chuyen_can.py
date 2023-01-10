n = int(input())
def check(s):
    msv, dd = [i for i in s.split()]
    sum = 10
    for i in dd:
        if i == 'v':
            sum -= 2
        elif i == 'm':
            sum -= 1
    if sum < 0: sum = 0
    return msv, sum
a = {}
for i in range(n):
    msv = input()
    ten = input()
    lop = input()
    a[msv] = [ten, lop]

for i in range(n):
    s = input()
    msv, diem_CC = check(s)
    a[msv] = a[msv] + [diem_CC]

for i in a:
    print(i, a[i][0], a[i][1], a[i][2], end=' ')
    if a[i][2] == 0:
        print('KDDK')
    else:
        print()

   
