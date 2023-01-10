t = int(input())
a={}
d= [0.0, 2.0, 1.5, 1.0, 0.0]
mon = {'TOAN': 'A', 'LY': 'B', 'HOA': 'C'}
for i in range(t):
    ten = input()
    ma = input()
    tin = float(input())
    cc = float(input())
    uutien = d[int(ma[1])]
    tong = tin*2+cc+uutien
    dict_val = list(mon.values())
    dict_key = list(mon.keys())
    sub = dict_key[dict_val.index(ma[0])]

    type = ''
    if tong >= 18.0: type = 'TRUNG TUYEN'
    else: type='LOAI'
    k = str(i+1)
    while(len(k)<2): k = '0'+k
    k = 'GV'+k
    a[k] = [ten, sub, tong, type]

a = sorted(a.items(), key=lambda x: -x[1][2])
for i in a:
    print(i[0], i[1][0], i[1][1], i[1][2], i[1][3])