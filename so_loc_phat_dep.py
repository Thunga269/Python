import math
import re
if __name__ == '__main__':
    s = input()
    s = s.replace('688','')
    s = s.replace('68','')
    s=  s.replace('6','')
    print('YES') if len(s) == 0 else print('NO')



