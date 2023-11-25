



products = {"HP":20, "DELL":50, "MACBOOK": 12, "ASUS":30}
prices = {"HP": 600, "DELL": 650, "MACBOOK": 1200, "ASUS": 400}

total_price = prices["ASUS"] * 5
print("total price:", total_price)

brand = input("input a brand: ")
amount = int(input("input amount to buy: "))
total_price = prices[brand] * amount 
print("total price:", total_price)

products[brand] = products[brand] - amount 

print("Available products: ") 
for key, value in products.items():
    print(key + ":", value)
    















































