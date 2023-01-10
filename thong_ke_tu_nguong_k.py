n, k = [int(x) for x in input().split()]
m = {}
for z in range(n) :
    s = input().lower()
    for i in s:
        if not i.isalpha() and not i.isnumeric():
            s = s.replace(i, ' ')
    for i in s.split():
        if i in m:
            m[i]+=1
        else:
            m[i]=1
m = sorted(m.items(), key = lambda x: (-x[1], x[0])) #xuất hiện giảm dần, từ điển tăng dần
for i in m :
    if i[1] >= k : 
        # print(i[0], i[1])
        print(*i)