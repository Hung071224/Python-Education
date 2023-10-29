#bài 1
sum = 0

n = int(input("Nhập n: "))

for i in range(n):
    x = int(input("Nhập x: "))
    # Kiểm tra nếu x là số chẵn
    if x % 2 == 0:
        sum += x

print("Tổng các số chẵn là:", sum)








#bài 2


count = 0

n = int(input("Nhập n: "))

for i in range(n):
    x = int(input("Nhập x: "))
    if x > 1:
        is_prime = True
        for j in range(2, int(x ** 0.5) + 1):
            if x % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1 

print("Số lượng số nguyên tố trong dãy là:", count)








#bài 3
max = int(input("Nhập phần tử đầu tiên: "))
index = 0

n = int(input("Nhập n: "))

for i in range(1, n):
    x = int(input("Nhập x: "))
    if x > max:
        max = x
        index = i

print("Vị trí của số lớn nhất trong dãy là:", index)








#bài 4



min = int(input("Nhập phần tử đầu tiên: "))
second_min = min

n = int(input("Nhập n: "))

for i in range(1, n):
    x = int(input("Nhập x: "))
    if x < min:
        second_min = min
        min = x
    elif x < second_min and x != min:
        second_min = x
        
print("Giá trị nhỏ thứ 2 trong dãy là:", second_min)







































































































