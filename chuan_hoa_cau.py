c = ".!?"
text = []
while True:
    try:
        line = input().strip().lower().split()
        if len(line) >0:
            if line[-1][-1] not in c: line += ['.'] # xét kí tự cuối cùng của phần tử cuối cùng -> VD:'te.'
        k = 0
        # print(line)
        for i in range(k, len(line)):
            if line[i][-1] in c:
                text.append(' '.join(line[k:i+1]))
                k = i+1

    except EOFError:
        break
for i in text: #i là 1 chuỗi
    i = i[:1].upper()+i[1:]
    if i[-1] in c and i[-2]==" ":
        i = i[:-2]+str(i[-1])
    print(i)