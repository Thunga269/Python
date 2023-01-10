P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True):
    n = input()
    if(n=='0'):
        break
    n = n.split()
    K = int(n[0])
    S = n[1]
    s = ""
    
    for i in S:
        j = P.find(i)
        s+= str(P[int((j+K)%28)])
    new_s = tuple(reversed(s))
    s = ''.join(new_s)
    print(s)
    
    
