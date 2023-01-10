t = int(input())
for i in range(t):
    dem = 0
    n = int(input())
    while(n>10):
        k = n%10
        n = n//10
        dem = dem +1
        if(k >= 5):
            n=n+1
    print(n*pow(10, dem))