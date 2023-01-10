kq = {}
for j in range(int(input())):
    name = input().strip().split()
    s=""
    for i in name:
        s += i[:1].upper()+i[1:].lower()+" "
    s = s.strip()
    d1, d2, d3 = float(input()), float(input()),float(input())
    tb = (d1*3+d2*3+d3*2)/8.0
    tb = "%.2f"%(tb+0.001)
    id = "SV%.2d"%(j+1)
    kq[id] = [s, tb]

kq = sorted(kq.items(), key=lambda x: (-float(x[1][1]), x[0]))
k, m, dem = 0, 0.0, 1
for i in kq:
    if m != i[1][1]:
        m = i[1][1]
        k += dem
        dem = 1
    else:
        dem += 1
    print(i[0], i[1][0], i[1][1], k)
