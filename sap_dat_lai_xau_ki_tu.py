import math
import re
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = list(input())
        s1.sort()
        s2 = list(input())
        s2.sort()
        print('Test '+str(i+1)+': ',end='')
        print('YES') if s1 == s2 else print('NO')