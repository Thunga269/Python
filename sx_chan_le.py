import math
if __name__ == '__main__':
    check=[]
    t = int(input())
    a= []
    even=[]
    odd=[]
    while t > 0 :
        b =[int(x) for x in input().split()]
        for i in b :
            a.append(i)
        t -= len(b)
    for i in a:
        check.append(int(i%2))
        if i%2==0: even.append(i)
        else : odd.append(i)
    even.sort()
    odd.sort(reverse=True)
    loop1 = 0 ; loop2 = 0
    for i in check:
        if i == 0 :
            print(even[loop1],end =  ' ')
            loop1 += 1
        else:
            print(odd[loop2],end=' ')
            loop2+=1






