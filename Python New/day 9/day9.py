



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
for i in range(1, 11):
    print(i, "is a prime number: ", isprimenumber(i))
































































































