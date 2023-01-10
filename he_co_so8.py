s = input()
res = ''
for i in range(len(s)-1,-1,-3):
    sum = 0
    
    sum += int(s[i])
    if i-1 >=0: sum+= 2*int(s[i-1])
    if i-2 >=0: sum+= 4*int(s[i-2])
    res += str(sum)
# print(res[::-1])