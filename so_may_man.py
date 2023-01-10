n = input()
dem = 0
for k in n:
    # print (k)
    
    if(k=='4' or k == '7'):
        dem = dem + 1
    if(dem > 7):
        break
    
if(dem == 4 or dem == 7):
    print("YES")
else:
    print("NO")