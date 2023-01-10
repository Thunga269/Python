m,n = map(int,input().split())
arr1 = [int(x) for x in input().split()]
arr1 = list(set(arr1))
arr2 =[int(x) for x in input().split()]
arr2 = list(set(arr2))
print('YES') if arr1==arr2 else print('NO')