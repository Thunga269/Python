n = int(input())
m = {}
for i in range(n) :
    ma = input()
    ten = input()
    ht = input()
    m[ma] = [ten, ht]

# print(m.items()): ('BAS', ['nhập môn AI', 'Vấn đáp'])
for i in sorted(m) : #sắp xếp theo mã môn
    print(i, m[i][0], m[i][1])
    
    