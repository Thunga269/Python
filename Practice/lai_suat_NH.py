'''
Lãi suất: X%
Tiền gửi vào: N
Sau mỗi năm tiền lãi cộng dần -> tiền đạt đc ít nhất là M
Tính số năm?
'''
import math
for _ in range(int(input())):
    N, X, M = [float(x) for x in input().split()]
    # M = N * (1+X%)^ năm = N * a ^ năm -> năm = log cơ số a của M/N
    a = (1+X/100)
    kq = math.log(M/N, a) 
    if(int(kq)<kq):
        print(int(kq)+1)
    else:
        print(kq)