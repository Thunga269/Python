if __name__ =='__main__':
    t = int(input())
    while t>0:
        t-=1
        n= int(input())
        arr = [int(x) for x in input().split()]
        arr =set(arr)
        print(max(arr)-min(arr)-len(arr)+1)