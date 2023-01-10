from typing import List



F = []
F.append(0)
F.append(1)
F.append(1)
F.append(2)

# for i in range(4, 93):
#     F.append(0)
for i in range(4, 93):
    F.append(F[i-1]+F[i-2])

t = int(input())

for j in range(t):
    a, b = [int(x) for x in input().split()]
    for i in range(a, b+1):
        print(F[i], end=" ")
    print()