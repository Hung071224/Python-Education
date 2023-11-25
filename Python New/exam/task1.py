



computer = {}

computer["Hp"] = 20
computer["DeLL"] = 50
computer["MACBOOK"] = 12   
computer["ASUS"] = 30   


print("available macbook:",computer.get("macbook"))

brand = input("input a brand: ")

print("available", brand + "s:", computer.get(brand.upper()))




























