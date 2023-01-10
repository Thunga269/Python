if __name__ =='__main__':
    str1 = input().lower().split()
    str2 = input().lower().split()
    se = set(str1+str2)
    se= list(se)
    
    se.sort()
    print(' '.join(se))
    se = set()
    for x in str2:
        if x in str1: se.add(x)
    se = list(se)
    se.sort()
    print(' '.join(se))

