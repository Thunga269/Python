t = int(input())
for k in range(t) :
    a = input()
    d, k = [], 1
    for i in a:
        if i =='(':
            print(k, end=' ')
            d.append(k)
            k+=1
        elif i==')':
            print(d[-1], end=' ') #in ra cái ngoặc gần nhất vừa push vào
            d.pop()
    print()