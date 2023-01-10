# m = "12345"
# print(m[-1])
for _ in range(int(input())):
    a, k = [], 1
    s = input()
    for i in s:
        # (( ))
        if i == '(':
            print(k, end=' ')
            a.append(k)
            k+=1
        elif i == ')':
            print(a[-1], end=' ')
            a.pop()
    print()
