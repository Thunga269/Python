t = int(input())
a = input()
a = a.split()

i = 0
b = []
while t > 0:
    t -=1
    x = int(a[i]) #lay phan tu trong day a
    i +=1
    if(len(b)>0):
        if((x + b[len(b)-1])%2==0): 
            b.pop() #xóa số cuối dãy và ko thêm số mới <-> xóa cả 2 số
        else:
            b.append(x)
    else: #nếu dãy b rống
        b.append(x)

print(len(b))
