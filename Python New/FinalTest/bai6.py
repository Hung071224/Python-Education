



n = int(input("Nhập vào 1 số nguyên >0: "))
if n <= 0: 
    print ("Sô bạn nhập không hợp lệ.")
else: 
    so_chu_so = 0
    while n > 0:
        so_chu_so += 1
        n //= 10
    print("Số chữ số của số bạn nhập là: ", so_chu_so)











































