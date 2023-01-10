from datetime import datetime
t = int(input())
tang = [0, 25, 34, 50, 80]
a={}
for i in range(t):
    ten = input().strip()
    soPhong = (input()).strip()
    ngayNhan = input().strip()
    ngayTra = input().strip()
    tienDV = int(input())
    #datetime.strptime: 1999-05-28 05:15:55.523000
    ngay = str(datetime.strptime(ngayTra, '%d/%m/%Y')-datetime.strptime(ngayNhan, '%d/%m/%Y')).split()[0] #trừ ra ngày
    if ngay == '0:00:00': ngay = 1
    else: ngay = int(ngay)+1
    tong = tang[int(soPhong[0])]*ngay + tienDV
    # print(tong)
    k = str(i+1)
    while(len(k)<2): k = "0" + k
    k = "KH" + k
    a[k] = [ten, soPhong, ngay, tong]

a = sorted(a.items(), key = lambda x: -(x[1][3]))

for i in a:
    print(i[0], i[1][0], i[1][1], i[1][2], i[1][3])



