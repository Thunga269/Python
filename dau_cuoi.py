t = int(input())
for i in range(0, t):
    a = input()
    l = int(len(a))

    # print(str(a[len-2])+str(a[len-1]))
    fir = str(a[0])+str(a[1])
    sec = str(a[l-2])+str(a[l-1])
    if(fir == sec):
        print("YES")
    else:
        print("NO")
