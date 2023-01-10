import numpy as np
# class Matrix:
#     def __init__(self, matrix1, matrix2) :
#         self.matrix1 = matrix1
#         self.matrix2 = matrix2
        
#     def Tich(self):
#         c = np.dot(self.matrix1, self.matrix2)
#         for i in range(len(c)):
#             for j in range(len(c)):
#                 print(c[i][j], end=' ')
#             print() 


t = int(input())
for i in range(t):
    N, M = [int(x) for x in input().split()]
    arr = []
    
    for j in range(N):
        a = [int(x) for x in input().split()]
        arr.append(a)
    arr = np.array(arr)   
    c = np.dot(arr, arr.T)
    
    
    for i in range(len(c)):
            for j in range(len(c)):
                print(c[i][j], end=' ')
            print() 

