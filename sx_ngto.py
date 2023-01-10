import math


def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0 : return False
    return n>1
if __name__ =='__main__':
    n = int(input())
    arr= [int(x) for x in input().split()]
    check=[0 for i in range(len(arr))]
    prime = list()
    for i in range(len(arr)):
        if isPrime(arr[i]):
            check[i] = 1
            prime.append(arr[i])
    prime.sort(reverse= True)
    for i in range(n):
        if check[i] ==0: print(arr[i],end=' ')
        else :
            print(prime[len(prime)-1],end=' ')
            prime.pop()
