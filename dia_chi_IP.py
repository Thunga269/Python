if __name__ =='__main__':
    t = int(input())
    while t>0:
        t-=1
        str= input().split('.')
        def isNumber(s):
            for x in s:
                if x<'0' or x>'9' : return False
            return True
        def isIp(str):
            if len(str) !=4 : return False
            for i in str:
                if isNumber(i) == False: return False
                if int(i) > 255 or int(i) < 0: return False
            return True
        print('YES') if isIp(str) else print('NO')

