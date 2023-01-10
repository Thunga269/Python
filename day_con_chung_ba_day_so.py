if __name__ =='__main__':
    t = int(input())
    while t>0:
        t-=1
        m,n,h = map(int,input().split())
        arr1 = [int (x) for x in input().split()]
        arr2 = [int (x) for x in input().split()]
        arr3 = [int (x) for x in input().split()]
        i =0; j=0;k=0;
        ok = 0
        while i<m and j<n and  k < h:
            if arr1[i] == arr2[j]  == arr3[k] :
                print(arr1[i],end =' ')
                ok=1
                i+=1; j+=1; k+=1
            elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]: i+=1
            elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]: j+=1
            else : k+=1
        if ok==0: print('NO',end='')
        print()
