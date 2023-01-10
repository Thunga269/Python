kq, TB = {}, 0
for i in range(int(input())):
    name = input()
    Arr=[float(x) for x in input().split()]
    
    TB = float("%.1f"% ((sum(Arr)+Arr[0]+Arr[1])/12.0+0.001))
    if TB < 5: XH = "YEU"
    elif TB < 7: XH = "TB"
    elif TB < 8: XH = "KHA"
    elif TB < 9: XH = "GIOI"
    else: XH = "XUAT SAC"
    kq["HS%.2d"%(i+1)] = [name, TB, XH]
kq = sorted(kq.items(), key = lambda x: (-x[1][1], x[0]))
for i in kq:
    print(i[0], i[1][0], i[1][1], i[1][2])