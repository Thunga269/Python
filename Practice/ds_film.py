class TheLoai:
    def __init__(self, id,name):
        self.id = id
        self.name = name

class Film:
    def __init__(self, id_f, id_theloai, day, name_f, num) :
        self.id_f = id_f
        self.theloai = map_TL[id_theloai]
        self.day = day
        self.name_f = name_f
        self.num = num
    def __str__(self) :
        return self.id_f+" "+self.theloai.name+" "+self.day+" "+self.name_f+" "+str(self.num)

N, M = map(int, input().split())
theloais = [TheLoai("TL%.3d"%(i+1),input()) for i in range(N)]
map_TL = {x.id: x for x in theloais}

films = [Film("P%.3d"%(i+1), input(), input(), input(), int(input())) for i in range(M)]
films.sort(key=lambda x: (x.day.split("/")[::-1], x.name_f, -x.num))
print(*films, sep='\n')
