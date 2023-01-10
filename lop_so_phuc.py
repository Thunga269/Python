class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def tich(self, p):
        thuc = self.thuc*p.thuc - self.ao*p.ao
        ao = self.thuc*p.ao+self.ao*p.thuc
        return SoPhuc(thuc, ao)
    def tong(self, p):
        thuc = self.thuc + p.thuc
        ao = self.ao + p.ao
        return SoPhuc(thuc, ao)

    def __str__(self):
        if(self.ao >= 0):
            return str(self.thuc) +" + "+str(self.ao)+"i"
        else:
            self.ao = -self.ao
            return str(self.thuc) +" - "+str(self.ao)+"i"

t = int(input())
for i in range(t):
    a, b, c, d=[int(x) for x in input().split()]
    A = SoPhuc(a, b)
    B = SoPhuc(c, d)
    c = A.tong(B)
    C = c.tich(A)
    D = c.tich(c)
    print(C, end=", ")
    print(D)