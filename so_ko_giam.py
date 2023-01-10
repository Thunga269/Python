t = int(input())
def check(n):
    l = len(n)-1
    for i in range(0, l):
        if(n[i]>n[i+1]):
            return False
    return True
for i in range(t):
    n = input()
    if(check(n)==True):
        print("YES")
    else:
        print("NO")