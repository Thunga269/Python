import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def RutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln
        print(str(int(self.tu))+"/"+str(int(self.mau)))
Arr = input().split()
PhanSo(int(Arr[0]), int(Arr[1])).RutGon()

        

        