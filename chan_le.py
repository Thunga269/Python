t = int(input())
def check(n):
    sum = int(0)
    for j in range(0, len(n)-1):
        sum += int(n[j])
        if ((int(n[j+1])-int(n[j])!=2) and (int(n[j+1])-int(n[j])!=-2)):
            return False
    sum += int(n[len(n)-1])
    #print(sum)
    if sum %10!=0:
        return False
    return True
for i in range(t):
    n = input()
    if(check(n)==True):
        print("YES")
    else:
        print("NO")
    
