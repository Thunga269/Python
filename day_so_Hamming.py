t = int(input())
N = 1000000000000000000
a=[]
import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1 ):
        if n%i:
            return False
    return True
def check():
    a.append(1)
    a.append(2)
    for n in range(3, N):
        for i in range(2, int(math.sqrt(n))+1):
            if N%i==0:
                if snt(i) and i <= 5 and i > max :
                    max = i
                if snt(n/i) and int(n/i)<=5 and(int(n/i))>max:
                    max = int(N/i)
        a.append(n)
for i in range(t):
    n = int(input())
    for j in range(len(a)):
        if a[j]==n:
            print(j+1)
        else:
            print("Not in sequence")
