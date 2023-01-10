t = int(input())
for i in range(t):
    N, d = [int(x) for x in input().split()]
    A = []
    
    for x in input().split():
        A.append(int(x))
    for i in range(d, len(A)):
        print(A[i], end=" ")
    for i in range(d):
        print(A[i], end=" ")
    print()

