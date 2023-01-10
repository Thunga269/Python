s = input()
if len(s)%2!=0: s = s[:len(s)-1]
arr = set()
for i in range(0,len(s),2):
    x = s[i]+s[i+1]
    arr.add(int(x))
arr = [str(x) for x in list(arr)]
print(' '.join(sorted(arr)))