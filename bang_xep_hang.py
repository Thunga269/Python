def check(s1, s2):
    return s1 > s2
class Student:
    def __init__(self, name, N, C):
        self.name = str(name)
        self.N = N
        self.C = C
    def __gt__(self, other):
        if self.N == other.N: 
            return self.C > other.C
        return self.N < other.N
        
    
a = []
t = int(input())
for i in range(t):
    name = input()
    N, C = [int(x) for x in input().split()]
    s = Student(name, N, C)
    a.append(s)
a = sorted(a)
for i in range (len(a)-1):
    for j in range (len(a)):
        if a[i].name < a[j].name:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
for i in sorted(a):
    print(i.name + " "+ str(i.N)+" "+str(i.C))
