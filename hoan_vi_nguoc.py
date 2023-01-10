from itertools import permutations
for _ in range(int(input())):
    n = int(input())
    perm1 = permutations(range(n, 0, -1))
    
    print(len(list(perm1)))
    perm = permutations(range(n, 0, -1))
    for i in list(perm):
        print(''.join((str(j) for j in i)), end = ' ')
    print()
