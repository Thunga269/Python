n = int(input())
a = []
s = ''
for i in range(n) :
    s = input()
    a.append(s)
    
    if(s==''):
        print(a[0]+':', len(a)-2)
        a.clear()
print(a[0]+':', len(a)-1)