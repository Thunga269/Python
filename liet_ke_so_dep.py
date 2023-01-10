t = int(input())
def check(n):
    s = n[::-1]
    if s!= n:
        return False
    if len(n)%2!=0:
        return False
    for i in n:
        if int(i)%2!=0:
            return False
    return True
for i in range(t):
    a = int(input())
    for j in range(22, a):
        if check(str(j))==True:
            print(j, end=" ")
    print()
    
            
                        