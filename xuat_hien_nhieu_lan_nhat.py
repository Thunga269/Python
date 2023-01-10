t = int(input())

b = []

for i in range(t):
    n = int(input())
    a = input().split()
    b.clear()
    max = 0
    for j in range(1000001):
        b.append(int(0))
    for j in a:
        b[int(j)]+=1
    for j in range(1000001):
        if(b[j] >=1):
            # print(str(j)+" " + str(b[j]))
            if b[max] < b[j]:
                max = j
                
    # max = max(b)
    # print(max)
    if float(b[max]) <= (n/2.0):
        print("NO")
    else:
        print(b[max])