
"""
#Bài 1

n = int(input("Nhập số n: "))
SC = 0
for k in range(1, n + 1):
    SC += 1 / k
print("SC =", round(SC,3))    

#Bài 2

bien_so = input("Nhập biển số xe: ")
hop_le = True
if len(bien_so) != 1:
    hop_le = False
else:
    if bien_so[3] != "-":
        hop_le = False
    elif bien_so[7] != ".":
        hop_le = False
    else:
        for i in range(10):
            if i == 3 or i ==7:
                continue
            if not (bien_so[i].ídigit() or bien_so[i].isalpha()):
                hop_le = False
                break
if hop_le:
    print("HOP LE")
else: 
    print("KHONG HOP LE")
        

#Bài 3
n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input(f"Nhập số nguyên thứ {i+1}: "))
    a.append(x)
dem = 0
for x in a:
    y = round(x ** 0.5)
    if y ** 2 == x:
        dem += 1
print(f"Có {dem} số chính phương trong dãy số")

"""

#Bài 4
n = int(input("Nhập n: "))
hang_hoa = {}
for i in range(n):
    ten = input(f"Nhập tên mặt hàng thứ {i+1}: ")
    gia = int(input(f"Nhập giá bán mặt hàng thứ {i+1}: "))
    hang_hoa[ten] = gia
max_hang = max(hang_hoa, key=hang_hoa.get)
min_hang = min(hang_hoa, key=hang_hoa.get)

print("Mặt hàng có giá bán lớn nhất là: ", max_hang, ":", hang_hoa[max_hang])
print("Mặt hàng có giá bán bé nhất là: ", min_hang, ":", hang_hoa[min_hang])


































































