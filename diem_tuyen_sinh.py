t = int(input())
KV = [0.0, 1.5, 1, 0.0]
a={}
for i in range(t):
    ten = input().strip().split()
    name = ''
    for j in ten:
        name += j[0:1].upper()+ j[1:].lower()+" "
    name = name.strip()
    diem = float(input())
    danToc = input()
    if danToc != "Kinh":
        diem += 1.5
    khuVuc = int(input())
    diem += KV[khuVuc]
    if diem < 20.5: type = 'Truot'
    else: type = 'Do'
    id = 'TS{0:0>2}'.format(i+1)
    a[id] = [name, diem, type]

a = sorted(a.items(), key = lambda x: (-x[1][1], x[0]))
for i in a:
    print(i[0], i[1][0], i[1][1], i[1][2])
