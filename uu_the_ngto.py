import math
t = int(input())
def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
        return True
for i in range(t):
    n = input()
    if check(len(n))==False:
        print("NO")
    else:
        dem = 0
        for i in n:

            if i!='2'and i!='3'and i!='5' and i !='7':
                dem+=1
        # print(dem)
        if len(n)-dem<=dem:
            print("NO")
        else:
            print("YES")