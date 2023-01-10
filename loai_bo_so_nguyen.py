def check(s):
    k = 0
    for i in s:
        if not i.isdigit():
            return True
        k = k*10 + int(i)

    if k <= 2147483647 and k >= -2147483648 :
        return False
    return True

file = open('DATA.in', 'r')
a = []
for i in file:
    for j in i.split():
        if(check(j)):
            a.append(j)
for i in sorted(a):
    print(i, end=' ')