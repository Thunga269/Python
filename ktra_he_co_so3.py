t = int(input())
for i in range(t):
    n = input()
    ok = 0
    for i in n:
        if i != '0' and i!='1' and i !='2':
            ok = 1
            break

    if ok == 0:
        print("YES")
    else:
        print("NO")