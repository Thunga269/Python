t = int(input())
a = {}
for i in range(t):
    ma = input()
    ten = input()
    soLuong = int(input())
    donGia = int(input())
    chietKhau = int(input())
    tong = donGia*soLuong- chietKhau
    a[ma] = [ten, soLuong, donGia, chietKhau, tong]
a = sorted(a.items(), key = lambda x: -x[1][4])
for i in a:
    print(i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4])
