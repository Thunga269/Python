if __name__ =='__main__':
    while True:
        t = int(input())
        if t == 0 : break
        arr =list()
        while t>0:
            t-=1
            arr.append(int(input()))
        if max(arr) == min(arr) : print('BANG NHAU')
        else : print(min(arr),max(arr))
