n = int(input())
arr=[]
for i in range(n):
    a = [int(x) for x in input().split()]
    arr.append(a)
sum1=sum2=0
K = int(input())
for i in range(n):
    for j in range(n):
        if i < j: #nua tren
            sum1+=arr[i][j]
        if j < i:
            sum2+=arr[i][j]
m=abs(sum1-sum2)

if(m<=K):
    
    print("YES")
else:
    print("NO")
print(m)