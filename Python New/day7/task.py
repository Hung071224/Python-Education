#bài 1

#nhập phần tử
# Bl: khai báo số lượng phần tử muốn nhập
n= int(input("Nhập số học sinh: "))
# B2: khai báo dictionary trổng
ds ={}
# B3: sử dụng vòng lặp for để nhập: key - value
for i in range(n):
    ten = input(f"- Nhập họ tên học sinh {i+1}: ")
    diem = float(input(f"- Nhập điểm trung bình học sinh {i+1}: "))
    # cách đẩy 2: sử dụng hàm update()
    ds.update(ften : diem?)
# sắp xếp theo chiêu giảm dân key
ds1 = dict(sorted(ds.items(), reverse = True))
# sắp xếp theo chiều tăng dần của value
ds2 = dict(sorted(ds. items (), key = lambda X .. x[1]))
print(ds1)
print(ds2)
        
        
        
        
        
        
        
        
#bài 2

def input_items(n):
    items = {}
    # Lặp n lần
    for i in range(n):
        name = input(f"Nhập tên của mặt hàng thứ {i+1}: ")
        price = float(input(f"Nhập giá bán của mặt hàng thứ {i+1}: "))
        items[name] = price
    return items
def display_max_min(items):
    max_item = max(items, key=items.get)
    min_item = min(items, key=items.get)
    print(f"Mặt hàng có giá bán lớn nhất: {max_item} : {items[max_item]}")
    print(f"Mặt hàng có giá bán nhỏ nhất: {min_item} : {items[min_item]}")
n = int(input("Nhập số nguyên dương n (mặt hàng): "))

items = input_items(n)

display_max_min(items)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    