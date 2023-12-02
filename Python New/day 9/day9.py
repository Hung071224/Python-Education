



#hàm cộng hai số
"""

def tong2so(a, b):
    tong = a + b
    return tong
print(tong2so(5, 10))

"""






#nhập các hệ số a, b,c 
"""
def nhap_đu_lieu():
    a = float(input("cho biết hệ số a: "))
    b = float(input("cho biết hệ số b: "))
    c = float(input("cho biết hệ số c: "))
    return a, b, c
"""


#hàm thực hiện 4 phép toán
"""

def pheptoan(a, b):
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b
    return tong, hieu, tich, thuong
    
"""


#phương trình có 2 nghiệm phân biệt
"""ư

def phuong_trinh_hai_nghiem(a, b, delta):
    x1 = (-b + sqrt(delta)) / (2 * a) #tính x1
    x2 = (-b - sqrt(delta)) / (2 * a) #tính x2
    print (f"phương trình có hai nghiệm: ")
    print (f"x1 = {1: .2f}, x2 = {x2: .2f}")
    
"""


#yêu cầu 1

"""

def isprimenumber(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n %2 == 0:
        return False
    for i in range (3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    
"""

"""
for i in range(1, 11):
    print(i, "is a prime number: ", isprimenumber(i))
    
"""


"""
import random
my_list = []
for i in range(10):
    num = random.randint(1, 100)
    my_list.append(num)
count = 0
print ("mylist: ", my_list)
for num in my_list:
    if isprimenumber(num):
        count +=1
    print("there are ", count, "prime numbers in my list")

"""


def nhap_bon_so(): 
    bon_so = []
    for i in range(4):
        so = float(input("nhập số thứ " + str(i+1) + ":"))
        bon_so.append(so)
    return bon_so


def tinh_trung_binh_cong(bon_so):
    tong = sum(bon_so)
    trung_binh_cong = tong / 4
    return trung_binh_cong    


def tim_so_lon_nhat(bon_so):
    so_lon_nhat = bon_so[0]
    for so in bon_so[1:]:
        if so > so_lon_nhat:
            so_lon_nhat = so
    return so_lon_nhat

def tim_so_nho_nhat(bon_so):
    so_nho_nhat = bon_so[0]
    for so in bon_so[1:]:
        if so < so_nho_nhat:
            so_nho_nhat = so
        return so_nho_nhat
bon_so = nhap_bon_so()
trung_binh_cong = tinh_trung_binh_cong(bon_so)
so_lon_nhat = tim_so_lon_nhat(bon_so)
so_nho_nhat = tim_so_nho_nhat(bon_so)
print ("Bốn số bạn đã nhập là: ", bon_so)    
print("Trung bình cộng của bốn số là: ", trung_binh_cong)
print("Số lớn nhất trong bốn sô là: ", so_lon_nhat)
print("Số nhỏ nhất trong bốn số là: ", so_nho_nhat)























































































