# t = int(input())
# import math
# result = []
# def distance(A, B):
#     return math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)
# for i in range(t):
#     m = [int(x) for x in input().split()]
#     A = [m[0], m[1]]
#     B = [m[2], m[3]]
#     C = [m[4], m[5]]
#     a = distance(A, B)
#     b = distance(B, C)
#     c = distance(A, C)
#     if max(a, b, c)*2 >= a+b+c:
#         result.append("INVALID")
#     else:
#         S = math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))/4
#         result.append(S)
#         # print('{:.2f}'.format(S))
# for i in result:
#     if i != 'INVALID':
#         print('{:.2f}'.format(i))
#     else:
#         print(i)
# from math import sqrt
import math

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def dis(self, p1, p2):
        return math.sqrt((p1.a-p2.a)**2+(p1.b-p2.b)**2)
    
    def cv(self):
        a = self.dis(self.p1, self.p2)
        b = self.dis(self.p1, self.p3)
        c = self.dis(self.p2, self.p3)
        if max(a, b, c)*2 >= a+b+c:
            return('INVALID')
        else :
            d = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            return('{:.2f}'.format(d))

arg = []
t = int(input())
for _ in range(t):
    arg += [float(i) for i in input().split()]
i = 0
for index in range(t):
    print(Triangle(Point(arg[i], arg[i+1]), Point(arg[i+2], arg[i+3]), Point(arg[i+4], arg[i+5])).cv())
    i += 6