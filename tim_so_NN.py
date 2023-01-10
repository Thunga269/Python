t = int(input())
for i in range(t):
    n = input()
    for j in n:
        if(j >= 'a' and j <= 'z'):
            n = n.replace(j, " ")
    s = n.split()
    
    if(len(s)==0):
        print("")
    else:
        h = []
        ok = int(0)
        for m in s:
            m = m.lstrip("0")
            if(len(m)==0): 
                ok = 1
                print("0")
                break
            else:
                k = int(m)
                h.append(k)
        if(ok==0):
            print(min(h))

     