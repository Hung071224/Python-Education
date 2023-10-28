#bai 1


"""

n = int(input("Nhập vào số lượng loại cá: "))
fish_list = []

for i in range(n):
    name = input(f"Nhập vào tên của loại cá thứ {i+1}: ")
    price = float(input(f"Nhập vào giá của loại cá thứ {i+1}: "))
    fish_list.append((name, price))
max_fish = fish_list[0] 
min_fish = fish_list[0] 
total_price = 0
for fish in fish_list:
    name, price = fish
    total_price += price
    if price > max_fish[1]:
        max_fish = fish
    if price < min_fish[1]:
        min_fish = fish
print(f"Loại cá có giá đắt nhất là {max_fish[0]} với giá {max_fish[1]}")
print(f"Loại cá có giá rẻ nhất là {min_fish[0]} với giá {min_fish[1]}")
print(f"Tổng giá các loại cá là {total_price}")



"""


#Bài 2



"""



n = int(input("Nhập vào số lượng cán bộ của khoa CNTT: "))

staff_list = []

obese_count = 0

for i in range(n):
    height = float(input(f"Nhập vào chiều cao của cán bộ thứ {i+1} (m): "))
    weight = float(input(f"Nhập vào cân nặng của cán bộ thứ {i+1} (kg): "))
    bmi = weight / (height ** 2)
    staff_list.append((height, weight, bmi))
    if bmi > 30:
        obese_count += 1


print("Danh sách chiều cao, cân nặng và BMI của các cán bộ: ")
print("Chiều cao (m) | Cân nặng (kg) | BMI | Đánh giá")
for staff in staff_list:
    height, weight, bmi = staff
    result = f"{height:.2f} | {weight:.2f} | {bmi:.2f} | "
    if bmi < 18.5:
        result += "Gầy"
    elif bmi < 25:
        result += "Bình thường"
    elif bmi < 30:
        result += "Thừa cân"
    else:
        result += "Béo phì"
    print(result)

print(f"Số lượng cán bộ béo phì của khoa CNTT là {obese_count}")



"""






















































































































































































