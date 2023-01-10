if __name__ =='__main__':
    n,k = map(int,input().split())
    se= set(input().upper().split())
    se = list(se)
    se.sort()
    n = len(se); pos = -1;
    str = ['' for i in range(n)]
    visited = [False for i in range(n)]
    def toHop(i):
        global pos
        for j in range(n):
            if j > pos and visited[j] == False:
                str[i] = se[j]
                visited[j]= True
                pos = j
                if i == k-1:
                    for h in range(k):
                        print(str[h],end = " ")
                    print()
                else: toHop(i+1)
                pos = -1
                visited[j] =False
    toHop(0)