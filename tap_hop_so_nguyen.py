m,n = map(int,input().split())
arr1 = [int(x) for x in input().split()]
arr1 = list(set(arr1))
arr2 =[int(x) for x in input().split()]
arr2 = list(set(arr2))
check = [0 for i in range(10000)]
for i in arr1: check[i]= 1
for i in arr2 :
    if(check[i]==1): check[i] = 2
    else: check[i] = 3
for i in range(10000):
    if(check[i]==2) : print(i,end=" ")
print()
for i in range(10000):
    if(check[i]==1) : print(i,end=" ")
print()
for i in range(10000):
    if(check[i]==3) : print(i,end=" ")