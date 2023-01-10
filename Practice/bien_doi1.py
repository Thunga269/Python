while(True):
    n = int(input())
    if n==0: break
    mp = {}
    mp[n]=1 # đánh dấu số đã tồn tại
    while n!= 1:
        if n%2==0:
            n /= 2
            mp[n]=1
        else:
            n = n*3+1
            mp[n]=1
    print(len(mp))
