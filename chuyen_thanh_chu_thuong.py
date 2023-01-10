s = input()
d = int(0)
len = len(s)
for c in range(len):
    if(s[c] >= 'A' and s[c] <='Z'): 
        d +=1
if(d > len-d):
    print(s.upper())
else:
    print(s.lower())