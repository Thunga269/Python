t = int(input())
for i in range(t):
    n = input()
    dem = 1
    s = ""
    for k in range(0, len(n)):
        if(k<(len(n)-1) and n[k]==n[k+1]):
            dem+=1
        else:
            s += str(dem)+n[k]
            dem = 1
    
    print(s)


