map = {}
def sapxep(n):
    return (0-n[1],n[0])

for _ in range(int(input())):
    s = input().lower()
    for i in range (len(s)):
        if not s[i].isalpha and not s[i].isnumeric():
            s = s.replace(s[i], ' ')
    for i in s.split():
        if i in map:
            map[i]+=1
        else:
            map[i]=1
map = sorted(map.items(), key=lambda ele: (-ele[1], ele[0]))
for i in map:
    print(*i) # ptit 4
    #print(i): ('ptit',4)
