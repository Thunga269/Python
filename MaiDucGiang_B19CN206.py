import re
from datetime import datetime
#xoa dau cua chu 
def xoadau(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s
#lay nam sinh
def get_year_206(day):
    day = day.split("/")
    return day[2]
#sinh user theo ten, ngaysinh
def get_username_Giang(hoten, day):
    hoten = xoadau(hoten)
    srr =hoten.lower()
    day = day.split("/")
    srr = srr.split()
    srr[-1] = srr[-1].lower()
    s = srr[-1]
    for ss in srr[0:-1]:
        s = s +ss[0]
    return s+day[2]
# def tinhphut(day):
#     day = day.split("/")
#     phut = int(day[0]) * 1440 + int(day[1]) * 


#tinh so phut toi thoi diem hien tai
def get_minute_206(time):
    now = str(datetime.now())
    now = now.split(" ")
    thungyathang = now[0].split()
    return time
#class thong tin nguoi dung
class NguoiDung_206:
    def __init__(self, ma, ten, birthday, loai, thoidiem) -> None:
        self.ma = ma
        self.ten = ten
        
        self.birthday = birthday
        self.nam = get_year_206(birthday)
        self.datatruyecap = Truycap_206(get_username_Giang(ten, birthday), loai, thoidiem)
#class thong tin truy cap
class Truycap_206:
    def __init__(self, user, loai, thoidiem) -> None:
        self.user = user
        self.loai = loai
        #thoi gian theo form: dd/mm/yyyy gio/phut/giay
        self.thoidiem = thoidiem
#"binh thuong" "nguy co thap" "nguy co cao" "tan cong"
per1 = NguoiDung_206(1, "Mai Duc giang1", "11/12/2001", "binh thuong", "22/12/2021 23:21:13")
per2 = NguoiDung_206(2, "Mai Duc giang2", "11/12/2002", "tan cong", "22/11/2021 06:21:13")
per3 = NguoiDung_206(3, "Mai Duc giang3", "7/12/2003", "nguy co thap", "20/12/2021 11:21:13")
per4 = NguoiDung_206(4, "Mai Duc giang4", "11/5/2004", "binh thuong", "2/12/2021 05:20:13")
per5 = NguoiDung_206(5, "Mai Duc giang5", "7/12/2005", "nguy co cao", "22/12/2021 01:01:13")
per6 = NguoiDung_206(6, "Mai Duc giang6", "11/9/2006", "binh thuong", "22/12/2021 05:21:13")

list_per = [per1, per2, per3, per4, per5, per6]

print("cau 2")
newlist = sorted(list_per, key=lambda x: x.nam, reverse=True)
for item in newlist:
	info =item.ten+'		'+item.datatruyecap.user+'		'+item.birthday
	print(info)
print("cau 3")
for item in list_per:
    if item.datatruyecap.loai == "nguy co cao" or  item.datatruyecap.loai == "tan cong":
        print(item.datatruyecap.user+'   '+item.datatruyecap.thoidiem+'   '+item.datatruyecap.loai )
print("cau 4")
dic = {}
x = []
y = []
for i in range(0, 24):
    x.append(i)
    y.append(0)
def get_gio(time):
    time = time.split(" ")
    time = time[1].split(":")
    return int(time[0])

for i in list_per:
    gio = get_gio( i.datatruyecap.thoidiem)
    y[gio] += 1
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=3)
ax.set_title("Bieu do thong tin truy cap", fontsize=24)
ax.tick_params(axis='both', labelsize=14)
plt.show()

