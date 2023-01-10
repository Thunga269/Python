a = []
a.append(0)
a.append(1)
a.append(1)
a.append(2)
for i in range(4, 93):
    a.append(a[i-1]+a[i-2])
for _ in range(int(input())):
    c, b = [int(x) for x in input().split()]
    for i in range(c, b+1):
        print(a[i], end=' ')
    print()
