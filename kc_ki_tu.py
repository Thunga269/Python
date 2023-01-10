import math
t = int(input())
def check(s1, s2):
    for i in range(len(s1)-1):
        sub1 = abs((ord(s1[i])-ord(s1[i+1])))
        sub2 = abs(ord(s2[i+1])-ord(s2[i]))
        if(str(sub1)!= str(sub2)):
            return False
    return True
for i in range(t):
    s1 = input()
    s2 = s1[::-1]
    
    if(check(s1, s2)==True):
        print("YES")
    else:
        print("NO")
    
    
        