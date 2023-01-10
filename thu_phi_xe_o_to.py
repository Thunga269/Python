a = {}
def check(xe, ghe):
    if xe == 'Xe_con':
        if ghe == 5: return 10000
        else: return 15000
    elif xe == 'Xe_tai':
        return 20000
    elif xe == 'Xe_khach':
        if ghe == 29: return 50000
        else: return 70000

for _ in range(int(input())):
    s = input().split()
    loai_xe = s[1]
    so_ghe = int(s[2])
    huong = s[3]
    ngay = s[4]
    if huong == 'IN':
        if ngay not in a:
            a[ngay] = check(loai_xe, so_ghe)
        else:
            a[ngay] += check(loai_xe, so_ghe)
#{'01/12/2022': [o to, 4]}        
a = sorted(a.items(), key=lambda x: x[0])
for i in a:
        print(str(i[0])+": "+str(i[1]))
