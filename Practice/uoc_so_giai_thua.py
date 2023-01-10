#Cho số tự nhiên N và số nguyên tố P. Nhiệm vụ của bạn là tìm số x lớn nhất để N! chia hết cho p mũ x. 
# Ví dụ với N=7, p=3 thì x=2 là số lớn nhất để 7! Chia hết cho 32. 
for i in range(int(input())):
    n, p = [int(x) for x in input().split()]
    dem = 0
    for j in range(1,n+1):
        k = j
        if k % p == 0:
            while(k % p == 0):
                dem += 1
                k /= p
    print(dem)
