#bai 1




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





#Bài 2


























































































































































































