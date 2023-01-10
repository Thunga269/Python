n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
maxi = max(arr[n-1]*arr[n-2],arr[0]*arr[1],arr[n-1]*arr[n-2]*arr[n-3],arr[n-1]*arr[0]*arr[1])
print(maxi)