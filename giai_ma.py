t = int(input())
for i in range(t):
    n = input()
    s = ""
    for k in range(0, len(n)+1):
        if k%2!=0:
            m = int(n[k])
            while(m>0):
                s+=n[k-1]
                m-=1
    print(s)
