#bai 1











































































#nhâp phan tu
# B1: khai báo số lượng phân tử muốn nhập
n= int(input("Nhập số người muốn thêm vào danh bạ: "))
# B2: khai báo dictionary trống
danhba = {}
# B3: sử dụng vòng lặp for để nhập: key - value
for i in range(n):
    ten = input(f"- Nhập họ tên người (i + 1): ")
    sdt = input(f"- Nhập số điện thoại người fi + 1):")
#cach day 1: su dung dinh nghia
    danhba[ten] = sdt
# cách đẩy 2: sử dụng hàm update()
    danhba.update({ten : sdt})



print (danhba)
































