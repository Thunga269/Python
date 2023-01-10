import math

if __name__ == '__main__':
    t = int(input())
    while t>0:
        t-=1
        n =int(input())
        a = [int(x) for x in input().split()]
        dic = {}
        for i in a:
            dic[i] = 0
        for i in a :
            dic[i] += 1
        res = 0
        dic_keys=list(dic.keys())
        dic_values=list(dic.values())
        for x in dic.values():
            if x%2!=0 : res = dic_keys[dic_values.index(x)]
        print(res)





