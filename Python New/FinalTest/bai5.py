



bang_gia = {
    "Samsung": {
        "Galaxy S23": 24000000,
        "Galaxys23 ultra": 32500000,
        "Galaxy z fold 4": 42000000
    },
    "Apple": {
        "iPhone 15": 27999999,
        "iPhone 15 pro": 32000000,
        "iPhone 15 pro max": 52000000
    },
    "Oppo": {
        "Reno 5": 9425000,
        "Find X2": 14750000,
        "A93": 5640000
    }
}

hang = input("Bạn muốn biết giá của hãng điện thoại nào? ")
model = input("Bạn muốn biết giá của model nào? ")

if hang in bang_gia and model in bang_gia[hang]:
    gia = bang_gia[hang][model]
    print("Giá của", hang, model, "là", gia, "đồng")
else:
    print("Không tìm thấy thông tin về", hang, model)
so_tien = int(input("Bạn có số tiền dự tính là bao nhiêu? "))

dien_thoai_phu_hop = []

for hang in bang_gia:
    for model in bang_gia[hang]:
        gia = bang_gia[hang][model]
        if gia <= so_tien:
            dien_thoai_phu_hop.append(hang + " " + model)

print("Những điện thoại có mức giá phù hợp với số tiền của bạn là:")
for dien_thoai in dien_thoai_phu_hop:
    print(dien_thoai)











































