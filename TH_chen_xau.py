s1 = input()
s2 = input()
t = int(input())
s = s1[:t-1]+ s2 + s1[t-1:]
print(s)