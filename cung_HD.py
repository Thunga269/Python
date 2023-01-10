t = input()
for i in range(int(t)):
    day, month = [int(x) for x in input().split()]
    if(month==3 or month==4):
        if(day>= 21 and month==3) or(day<=19 and month==4):
            print("Bach Duong")
    if(month==4 or month==5):
        if(day>= 20 and month==4) or(day<=20 and month==5):
            print("Kim Nguu")
    if(month==5 or month==6):
        if(day>= 21 and month==5) or(day<=20 and month==6):
            print("Song Tu")    
    if(month==6 or month==7):
        if(day>= 21 and month==6) or(day<=22 and month==7):
            print("Cu Giai")
    if(month==7 or month==8):
        if(day>= 23 and month==7) or(day<=22 and month==8):
            print("Su Tu")
    if(month==8 or month==9):
        if(day>= 23 and month==8) or(day<=22 and month==9):
            print("Xu Nu")
    if(month==9 or month==10):
        if(day>= 23 and month==9) or(day<=22 and month==10):
            print("Thien Binh")
    if(month==10 or month==11):
        if(day>= 23 and month==10) or(day<=22 and month==11):
            print("Thien Yet")
    if(month==11 or month==12):
        if(day>= 23 and month==11) or(day<=21 and month==12):
            print("Nhan Ma")
    if(month==12 or month==1):
        if(day>= 22 and month==12) or(day<=19 and month==1):
            print("Ma Ket")
    if(month==1 or month==2):
        if(day>= 20 and month==1) or(day<=18 and month==2):
            print("Bao Binh")
    if(month==2 or month==3):
        if(day>= 19 and month==2) or(day<=20 and month==3):
            print("Song Ngu")                