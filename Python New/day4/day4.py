#bài 1




"""

a= float(input("nhập vào số thực dương a : "))
b= float(input("nhập vào số thực dương b : "))
c= float(input("nhập vào số thực dương c : "))

S1= a**2 - 2*b + a*b/(c**2 + 3)

#a

print (f"Giá trị của biểu thức S1 = {S1 : .3f}")

#b

S2 = (b**2 - 4*a*c)/(2*a)
print (f"Giá trị của biểu thức S2 = {S2 : .3f}")

#c

S3 = 3*a - b**3 + 2*(c**2 + 1)**0.5
print (f"Giá trị của biểu thức S3 = {S3 : .3f}")

#d

S4 = (a**2/b - (4*a)/(b*c) +1 )**0.5
print (f"Giá trị của biểu thức S4 = {S4 : .3f}")




"""





#bài 2




"""

điểm_toán = float(input("Nhập điểm toán : "))
điểm_lý = float(input("nhập điểm lý : "))
điểm_hóa = float(input("nhập diểm hóa : "))

dtb = (điểm_toán + điểm_lý + điểm_hóa) / 3

if dtb >= 8:
    xếp_loại = "A"
elif dtb >= 6.0:
    xếp_loại = "B"
elif dtb >= 4.0:
    xếp_loại = "C"

else:
    xếp_loại = "D"

print (f"Điểm trung bình của học sinh là :{dtb: .2f}")
print (f"xếp loại học sinh là: {xếp_loại}")





"""



#bài 3



"""
# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra điều kiện n > 0
if n > 0:
    # Khởi tạo các biến S1, S2 và S3
    S1 = 0
    S2 = 0
    S3 = 0

    # Tính tổng S1 bằng vòng lặp for
    for i in range(1, n + 1):
        S1 += 1 / (i * (i + 1))

    # Tính tổng S2 bằng vòng lặp while
    i = 0
    while i < n:
        S2 += 3 ** (1 / 3) # Căn bậc ba của 3
        i += 1

    # Tính tổng S3 bằng vòng lặp do-while (sử dụng break để thoát khỏi vòng lặp)
    i = 1
    sum = 0 # Biến lưu trữ tổng các số từ 1 đến i
    while True:
        sum += i
        S3 += 1 / sum
        i += 1
        if i > n: # Điều kiện dừng vòng lặp
            break

    # In kết quả ra màn hình với định dạng có 3 chữ số sau dấu phẩy
    print(f"S1 = {S1:.3f}")
    print(f"S2 = {S2:.3f}")
    print(f"S3 = {S3:.3f}")
else:
    # In thông báo lỗi nếu n không thỏa mãn điều kiện
    print("n phải là số nguyên dương!")
"""









#bài 4

"""

# Nhập số nguyên dương N
N = int(input("Nhập số nguyên dương N: "))

# Kiểm tra điều kiện N > 0
if N > 0:
    # Khởi tạo biến đếm số dấu * trên mỗi hàng
    count = 1

    # Tính khoảng cách giữa dấu * đầu tiên và cuối cùng trên hàng cuối cùng
    distance = 2 * N - 1

    # In tam giác cân bằng vòng lặp for
    for i in range(1, N + 1):
        # In khoảng trắng trước dấu * đầu tiên
        print(" " * ((distance - count) // 2), end="")

        # In dấu * trên mỗi hàng
        print("*" * count)

        # Tăng biến đếm lên 2
        count += 2
else:
    # In thông báo lỗi nếu N không thỏa mãn điều kiện
    print("N phải là số nguyên dương lớn hơn 0!")


"""









































