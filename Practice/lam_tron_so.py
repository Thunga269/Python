for _ in range(int(input())):
    dem = 0
    n = int(input())
    while(n>10):
        k = n%10
        n = n//10
        dem += 1
        if(k >= 5):#Nếu chữ số >= 5 thì tăng số chữ số đằng trước lên 1 đơn vị
            n += 1
    print(n*pow(10,dem)) #10^dem
    