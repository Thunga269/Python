def isOk(s):
    if s.count('A') >0 and s.count('C') >= s.count('B') and s.count('B')>=s.count('A'):
        return True
    return False
def backTrack(n,s):
    if s.count('A')> n/3 or s.count('B')+ s.count('A') > 2*n/3:
        return
    if len(s) == n:
        if isOk(s):
            print(s)
    elif len(s) < n :
        backTrack(n,s+'A')
        backTrack(n,s + 'B')
        backTrack(n,s + 'C')
if __name__ =='__main__':
    n = int(input())
    for i in range(3,n+1):
        backTrack(i,'')