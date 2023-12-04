

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
# 2023-12-04 20:26:04.000000
print(now.strftime('%Y/%m/%d'))
# 2023/12/04
print(now.strftime('%H:%M:%S %Y-%m-%d'))
# 20:26:04 2023-12-04

"""

#sửa
from datetime import datetime
now = datetime.now()
print(f"Today is {now.strftime('%d/%m/%Y')}")
# Today is 04/12/2023
print(f"Time right now: {now.strftime('%H:%M:%S')}")
# Time right now: 20:26:04





























