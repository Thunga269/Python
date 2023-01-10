from datetime import datetime

class Subject:
    def __init__(self, id: str, name: str, exam_format: str):
        self.id = id
        self.name = name
        self.exam_format = exam_format
    
    def __str__(self):
        return self.name
    
    
class Shift:
    order = 1
    
    def __init__(self, day: str, time: str, room: str):
        self.id = f'C{Shift.order:03}'
        self.time = datetime(int(day[6:]), int(day[3:5]), int(day[:2]), int(time[:2]), int(time[3:]))
        self.room = room
        Shift.order += 1
    
    def __str__(self):
        return self.time.strftime('%d/%m/%Y %H:%M ') + self.room
    
    def __lt__(self, other):
        return self.time < other.time
    
    
class Schedule:
    def __init__(self, subject: Subject, shift: Shift, group: str, number_of_attendee: str):
        self.subject = subject
        self.shift = shift
        self.group = group
        self.number_of_attendee = number_of_attendee
    
    def __str__(self):
        return str(self.shift) + ' ' + str(self.subject) + ' ' + self.group + ' ' + self.number_of_attendee

    def __lt__(self, other):
        return self.shift < other.shift

subjects = {}

with open('MONTHI.in') as f:
    f1 = f.readlines()

for i in range(1, int(f1[0])*3+1, 3):
    id, name, exam_format = f1[i].rstrip(), f1[i+1].rstrip(), f1[i+2].rstrip()
    subjects[id] = Subject(id, name, exam_format)
    
    
with open('CATHI.in') as f:
    f2 = f.readlines()

shifts = [Shift(f2[i].rstrip(), f2[i+1].rstrip(), f2[i+2].rstrip()) for i in range(1, int(f2[0])*3+1, 3)] 


with open('LICHTHI.in') as f:
    f3 = f.readlines()

schedules = []
for i in range(1, int(f3[0])+1):
    shift, subject, group, number_of_attendee = f3[i].rstrip().split(' ')
    shift = shifts[int(shift[1:])-1]
    subject = subjects[subject]
    schedules.append(Schedule(subject, shift, group, number_of_attendee))
    
schedules.sort()
for schedule in schedules:
    print(schedule)