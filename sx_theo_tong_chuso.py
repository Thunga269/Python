t = int(input())

def myFunc(x):
    x = str(x)
    sum=0
    for i in x:
        sum += int(i)
    return sum
for j in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a.sort(key=myFunc)
    for i in a:
        print(i, end=" ")
    print()
