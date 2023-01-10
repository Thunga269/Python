class Student:
    def __init__(self, name, date, d1, d2, d3):
        self.name = name
        self.date = date
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.sum = d1+d2+d3

    

name = input()
date = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
s = Student(name, date, d1, d2, d3)
print(s.name +" "+s.date+" ", end='')
print("%.1f" %s.sum)