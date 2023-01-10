import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def RutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln
        return PhanSo(int(self.tu), int(self.mau))
    def Tong(self, p):
        ucln = math.gcd(self.mau, p.mau)
        t = self.tu * (p.mau/ucln) + (self.mau/ucln) * p.tu
        m = (self.mau*p.mau)/ucln
        return PhanSo(int(t), int(m))
    def __str__(self):
        return (str(int(self.tu))+"/"+str(int(self.mau)))
Arr = input().split()
p1 = PhanSo(int(Arr[0]), int(Arr[1])).RutGon()
p = PhanSo(int(Arr[2]), int(Arr[3])).RutGon()
# print(p1)
# print(p)
res = p1.Tong(p)
print(res)
