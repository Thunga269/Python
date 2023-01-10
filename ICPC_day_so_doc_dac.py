t = int(input())
set = set()
for i in range(t):
    n = int(input())
    a = input().split()
    set.clear()
    for j in a:
        set.add(j)
    ok = 0
    for j in set:
        if(a.count(j)==1):
            print("YES")
            ok = 1
            break
    if ok == 0:
        print("NO")
    