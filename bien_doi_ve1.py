import  collections
def myFunc():
    return 0

while True:
    n = int(input())
    if n==0: break
    mp = collections.defaultdict(int)
    mp[n]=1
    while n!=1:
        if n%2==0:
            n/=2
            mp[n]=1
        else:
            n=3*n+1
            mp[n]=1
    print(len(mp))
