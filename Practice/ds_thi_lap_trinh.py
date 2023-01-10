class Team:
    def __init__(self, id_team, name_team, name_school) :
        self.id_team = id_team
        self.name_team =name_team
        self.name_school= name_school

class Student:
    def __init__(self, id_stu, name_stu, id_team):
        self.id_stu = id_stu
        self.team = map_team[id_team]
        self.name_stu = name_stu
        # self.id_stu=id_stu
    def __str__(self):
        return self.id_stu +" "+self.name_stu+" "+self.team.name_team+" "+self.team.name_school

t1 = int(input())
teams = [Team("Team%.2d"%(i+1),input(), input()) for i in range(t1)]
map_team = {i.id_team: i for i in teams}

t2 = int(input())
students = [Student("C%.3d"%(i+1), input(), input()) for i in range(t2)]
students.sort(key = lambda x: x.name_stu)
print(*students, sep='\n')
