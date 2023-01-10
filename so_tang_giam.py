import math
t = int(input())
for i in range(t):
    n = input()
    if(len(n)<3):
        print("NO")
    else:
        dem_t = 0
        dem_g = 0
        c = 0
        m = int(n[1])-int(n[0])
        for i in range(0, len(n)-1):
            if int(n[i+1])-int(n[i])>0: 
                dem_t += 1
            else:
                c = i
                break
        p = int(n[c])-int(n[c+1])
        # print(p)
        for i in range(c, len(n)-1):
            if int(n[i])-int(n[i+1])>0: 
                dem_g += 1
            else:
                break
        # print(dem_g)
        # print(dem_t)
        if dem_g+dem_t==len(n)-1:
            print("YES")
        else:
            print("NO")
