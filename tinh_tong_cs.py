import math
import re
if __name__ == '__main__':
    t = int (input())
    while t>0:
        t-=1
        s = input()
        num = re.findall('\d',s)
        sum = 0
        string = re.findall('\D',s)
        string.sort()
        for x in num : sum+=int(x)
        for x in string : print(x,end = '')
        print(sum)