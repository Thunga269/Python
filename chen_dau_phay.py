m = input()
n = m[::-1]
s = ""
k = int(len(n)//3)
for i in range(0, k*3, 3):
    s += n[i:i+3]+","
if(len(n)%3!=0):
    s += n[k*3:len(n)+1]
else:
    s = s[:len(s)-1]
print(s[::-1])

