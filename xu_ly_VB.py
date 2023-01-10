text = ""
while True:
    try: 
        n = input()
        text += n+" "
    except EOFError: 
        break

c = (". ? !").split()
text = " ".join(text.split())
for i in c:
    text = text.replace(i, '.')
text = text.lower()
s = text.split(".")
result = ""
for i in s:
    i=i.strip()
    result = str(i[0:1].upper()) + str(i[1:len(i)])
    print(result)

# import re
# Data = "Hey, you - what    are you doing  !?"
# print (re.findall(r"[\w]+", Data))