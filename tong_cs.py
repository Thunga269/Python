
s = input()
d=0
while(len(s)>1):
    n = 0
    for i in s:
        n+= (ord(i)-ord('0')) #in ra số ban đầu
    s = str(n)
    d+=1
print(d)