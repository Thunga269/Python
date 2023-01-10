a = {'A': [10, 12, 14, 20], 'B': [10, 11, 13, 16], 'C':[9, 10, 12, 14], 'D':[8, 9, 11, 13]}
class Phong:
    def __init__(self, args):
        self.id = args[:2]
        self.name = args[3:]

class NhanVien:
    def __init__(self, id_NV, name_NV, luongCB, ngaycong):
        self.id_nv = id_NV
        self.phong = map_phong[id_NV[-2:]]
        self.name_nv = name_NV
        self.luongCB = luongCB
        self.ngaycong = ngaycong
        self.nam = int(id_NV[1:3])
        self.salary = 0
        s = a[id_NV[0]]
        if self.nam >= 1 and self.nam <= 3:
            self.salary += self.luongCB*self.ngaycong*s[0]
        elif self.nam >= 4 and self.nam <= 8:
            self.salary += self.luongCB*self.ngaycong*s[1]
        elif self.nam >= 9 and self.nam <= 16:
            self.salary += self.luongCB*self.ngaycong*s[2]
        elif self.nam >= 16:
            self.salary += self.luongCB*self.ngaycong*s[3]

    def __str__(self) :
        return self.id_nv +" "+self.name_nv+" "+self.phong.name+" "+str(self.salary*1000)

t = int(input())
phongs = [Phong(input()) for _ in range(t)]
map_phong = {i.id: i for i in phongs}

t2 = int(input())
nhanviens = [NhanVien(input(), input(), int(input()), int(input())) for _ in range(t2)]
print(*nhanviens, sep='\n')
