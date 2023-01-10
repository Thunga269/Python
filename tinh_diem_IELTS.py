
def getScore(x):
    if x>=39: return 9;
    if x>=37 :return 8.5;
    if x>=35: return 8.0;
    if x>=33: return 7.5;
    if x>=30: return 7;
    if x>=27 :return 6.5;
    if x>=23 :return 6;
    if x>=20: return 5.5;
    if x>=16: return 5;
    if x>=13: return 4.5;
    if x>=10 :return 4;
    if x>=7:return 3.5;
    if x>=5 :return 3;
    return 2.5;
t = int(input())
while t>0:
    t-=1
    x,y,d3,d4 = map(float,input().split())
    d1 = getScore(x)
    d2= getScore(y)
    avg = (d1+d2+d3+d4)*0.25
    z = avg - int(avg)
    if z < 0.25: avg = int(avg)
    elif z == 0.25: avg += 0.25
    elif z<0.75: avg =int(avg)+0.5
    else : avg = int(avg)+1
    print(format(avg,'.1f'))