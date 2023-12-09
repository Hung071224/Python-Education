

#bài 1
"""

def is_int(num):
    return num - int(num) == 0
num = float(input("nhập vào một số thực: "))
if is_int(num):
    print(f"{int(num)} là số nguyên ")
else:
    print(f"{int(num)} không phải là số nguyên ")
    
"""

#bài 2

"""
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num ==3:
        return True
    if num % 2 == 0 or num % 3== 0:
        return False
    i = 5 
    while i * i <= num:
        if num % i ==0 or num % (i+2) == 0:
            return False
        i += 6
        return True
num = int(input("Nhập vào một số nguyên: "))
if í_prime(num):
    print(f"{num} là số nguyên tố ")
else: print(f"{num} không là số nguyên tố")

"""


#bài 3

"""
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num ==3:
        return True
    if num % 2 == 0 or num % 3== 0:
        return False
    i = 5 
    while i * i <= num:
        if num % i ==0 or num % (i+2) == 0:
            return False
        i += 6
        return True
n = int(input("Nhập vào một số nguyên dương: "))
count = 0
num = 2
print(f"{num} số nguyên tố đầu tiên là: ")
while count < n:
    if is_prime(num):
        print(num, end= " ")
        count += 1
    num+=1

"""




#bài 4
    
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)
n = int(input("Nhấp vào một số nguyên dương: "))
sum = 0
for i in range(1, n + 1):
    sum += factorial(i) / i

print(f"Giá trị của biểu thức 1!/1 + 2!/2 + .... + n!/n là: {sum}")

"""





#bài 5


#chưa sửa 
"""

from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime('%Y/%m/%d'))
print(now.strftime('%H:%M:%S %Y-%m-%d'))

"""

#sửa

"""

from datetime import datetime
now = datetime.now()
print(f"Today is {now.strftime('%d/%m/%Y')}")

print(f"Time right now: {now.strftime('%H:%M:%S')}")


"""




#bài nâng cao  (." ^ ".)



def nam_nhuan(nam):
    if (nam % 4 ==0 and nam %100 != 0) or (nam % 400 ==0):
        return True
    else: 
        return False
def so_ngay(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10,12]:
        return 31
    elif thang ==2:
        if nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return 30
def ngay_truoc_sau(ngay, thang, nam):
    if nam < 1 or thang < 1 or thang > 12 or ngay < 1 or ngay > so_ngay(thang, nam):
        print("Ngày, tháng, năm không hợp lệ!")
        return
    if ngay ==1:
        if thang == 1:
            ngay_truoc = 31
            thang_truoc = 12
            nam_truoc = nam - 1
        else: 
            ngay_truoc = so_ngay(thang - 1, nam)
            thang_truoc = thang - 1
            nam_truoc = nam
    else:
        ngay_truoc = ngay -1
        thang_truoc = thang
        nam_truoc = nam
    if ngay == so_ngay(thang, nam):
        if thang ==12:
            ngay_sau = 1
            thang_sau = 1
            nam_sau = nam + 1
        else:
            ngay_sau = 1
            thang_sau = thang +1
            nam_sau = nam
    else:
        ngay_sau = ngay +1
        thang_sau = thang 
        nam_sau = nam
    print(f"Trước đó là{ngay_truoc:02d}/{thang_truoc:02d}/{nam_truoc:04d}")
    print(f"Sau đó là {ngay_sau:02d}/{thang_sau:02d}/{nam_sau:04d}")
ngay = int(input("Nhập ngày: "))
thang = int(input("nhập tháng: "))
nam = int(input("nhấp năm: "))
ngay_truoc_sau(ngay, thang, nam)
            


















