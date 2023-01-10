
class Subject:
    def __init__(self, id, name) :
        self.id = id
        self.name = name 

class Exam:
    def __init__(self, ex_id, args):
        self.ex_id = ex_id
        self.subject = map_sub[args[0]]
        self.day = args[1]
        self.time = args[2]
        self.shift = args[3]
    
    def __str__(self):
        return self.ex_id + " "+ self.subject.id+" "+self.subject.name+" "+self.day+" "+self.time+" "+self.shift

N, M = [int(x) for x in  input().split()]
subjects = [Subject(input(), input()) for _ in range(N)]

map_sub = {i.id: i for i in subjects} #INT1155 : 1 class có ID là INT1155

exames = [Exam("T%.3d"%(i+1), input().split() ) for i in range(M)]
exames.sort(key=lambda x: (x.day.split("/")[::-1], x.time, x.subject.id)) #sắp xép theo năm/tháng/ngày
print(*exames, sep='\n')