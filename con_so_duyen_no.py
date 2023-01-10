from imaplib import Int2AP


t = int(input())
for i in range(t):
    n = input()
    if n[0]==n[len(n)-1]:
        print("YES")
    else:
        print("NO")