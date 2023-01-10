import math
t = int(input())
for i in range(t):
    n = input()
    if(len(n)<2):
        print("NO")
    else:
        sum = 0
        for i in n:
            sum += int(i)
        sum = str(sum)
        if(len(sum)<2):
            print("NO")
        else:
            s = sum[::-1]
            # print(s)
            if(s==sum):
                print("YES")
            else:
                print("NO")