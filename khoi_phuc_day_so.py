n = int(input())
a=[]
arr=[]
b=[]
s=0
for i in range(n):
    a = [int(x) for x in input().split()]
    b.append(sum(a))
    s += b[-1] #cộng với phần tử vừa đc thêm vào
# print(b)
if n == 2 :
    for i in b :
        print(int(i / 2), end = ' ')
else :
    s = int(s / 2 / (n - 1)) #s/2: TB tổng nửa trên; (s/2)/(n-1): Tb tổng từng dòng nửa trên
    # print(s)
    for i in b :
        print(int((i - s) / (n - 2)), end = ' ')
