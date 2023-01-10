dic = {}
t, k = [int(x) for x in input().split()]
for _ in range(t):
    s = input().lower()
    for i in s:
        if not (i.isalpha() or i.isdigit()):
            s = s.replace(i, " ")
   
    for i in s.split():
        if i in dic:
            dic[i] += 1
        else: 
            dic[i] = 1
dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
# print(dic)
for i in (dic):
    if i[1] >= k:
        print(*i)
        # print(i[0], i[1])
