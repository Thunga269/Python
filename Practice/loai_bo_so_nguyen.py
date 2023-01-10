def check(s):
    for i in s:
        if not i.isdigit():
            return True
    k = int(s)      
    if k <= (2**31-1) and k >= -(2**31) :
        return False
    return True

a=[]
f = open("Practice\VANBAN.in", 'r')
for i in f.readlines():
    i = i.strip().split()
    for j in i:
        if check(j):
            a.append(j)
for i in sorted(a):
    print(i,end=' ')
