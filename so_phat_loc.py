t = int(input())
for i in range(t):
    n = input()
    l = len(n)-1
    if(n[l-1]=='8' and n[l]=='6'):
        print("YES")
    else:
        print("NO")