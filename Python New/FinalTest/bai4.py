








mon_da_goi = []
dat_them = True
while dat_them:
    mon = input("Bạn muốn đặt món gì? ")
    if mon in mon_da_goi:
        print(mon, "đã được gọi")
    else:
        mon_da_goi.append(mon)
        print("Đã thêm,", mon, "vào list")
    cau_hoi = input("Bạn có muốn đặt thêm gì không? (Có/Không)")
    if cau_hoi.lower() == "không":
        dat_them = False
print("Những món bạn đã đặt là: ")
for mon in mon_da_goi:
    print(mon)





















































