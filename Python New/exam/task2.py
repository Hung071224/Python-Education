



products = {"HP":20, "DELL":50, "MACBOOK": 12, "ASUS":30}

print("available MAcBOOKS:", products["MACBOOK"])

brand = input("input a brand: ")
print("available", brand + "s:", products[brand])
products["TOSHIBA"] = 10
print("available product: ") 
for key, value in products.items():
    print(key + ":", value)

new_brand = input("input a new brand: ")
new_amount = int(input("input a new amount: "))
products[new_brand] = new_amount

print("available products: ") 
for key, value in products.items():
    print(key + ":", value)

products["DELL"] = 60
products["MACBOOK"] = 2

print("available product: ") 
for key, value in products.items():
    print(key + ":", value)
total = 0
for value in products.values():
    total += value 
print("Total products:",total)






































