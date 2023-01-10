import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return  False
    return n>1
if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    dic = {}
    
    for i in a:
        if isPrime(i): dic[i]=0
    for i in a:
        if isPrime(i): dic[i]+=1
    for x, y in dic.items():
        print(x, y)




