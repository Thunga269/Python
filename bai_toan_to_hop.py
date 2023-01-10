from fileinput import hook_compressed
import itertools
n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr = set(arr)
arr = list(arr)
arr.sort()
arr = map(str,arr) #chuyen sang str
# print(arr)
comb = itertools.combinations(arr,k)
for x in comb:
    # print(x)
    print(' '.join(x))
# itertools.combinations: to hop 
# itertools.permutations: hoan vi 
