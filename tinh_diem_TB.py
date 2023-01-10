t = int(input())
a={}
for k in range(t):
    ten = input().strip().split()
    name = ''
    for i in ten:
        name += i[0:1].upper()+i[1:].lower()+" "
    name = name.strip()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    ma = 'SV{0:0>2}'.format(k+1)
    
    TB = '{:.2f}'.format((d1*3 + d2*3 + d3*2)/8+0.001)
    
    a[ma]= [name,TB]

a = sorted(a.items(), key = lambda x: (-float(x[1][1]), x[0]))
k = 0
m = 0.0
dem = 1
for i in a:
    if i[1][1] != m:
        m = i[1][1]
        k+=dem
        dem = 1
    else: dem +=1
    print(i[0], i[1][0], i[1][1], k)




