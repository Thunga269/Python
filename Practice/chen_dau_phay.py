#phân tách các nhóm 3 chữ số (tính từ cuối). Ví dụ số 153920529 được viết lại thành 153,920,529.
s = input()
dem = 0
while len(s)%3!=0: 
    s = "0"+s
    dem += 1
kq = ""
for i in range(0,len(s),3):
    kq += s[i:i+3]+","
print(kq[dem:].strip(','))
