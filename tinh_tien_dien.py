t = int(input())
def chuanHoa(s):
    s = input().strip().split()
    name = ''
    for i in s:
        name += i[0:1].upper()+i[1:].lower()
    return name 

a = {}
norm = {'A':100, 'B':500, 'C':200}
for j in range(t):
    s = input().strip().split()
    name = ''
    for i in s:
        name += i[0:1].upper()+i[1:].lower()+ " "
    name= name.strip()
    loaiGD, dau, cuoi = [ x for x in input().split()]
    dau = int(dau)
    cuoi = int(cuoi)
    DM = norm[loaiGD]
    soDien = cuoi-dau

    if soDien < DM: 
        tienTrong=soDien*450
    else: 
        tienTrong = DM*450
        
    if soDien > DM: tienVuot =(soDien-DM)*1000
    else: tienVuot=0

    thueVat = tienVuot//20
    tong = tienTrong+tienVuot+thueVat
    ma = 'KH{0:0>2}'.format(j+1)
    a[ma] = [name, tienTrong, tienVuot, thueVat, tong]

a = sorted(a.items(), key = lambda x: -x[1][4])
for i in a:
    print(i[0], i[1][0], i[1][1], i[1][2] ,i[1][3], i[1][4])

    

