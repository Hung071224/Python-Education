



products = {"HP":20, "DELL":50, "MACBOOK": 12, "ASUS":30}
prices = {"HP": 600, "DELL": 650, "MACBOOK": 1200, "ASUS": 400}

total_value= {}
for key in products:
    total_value[key] =products[key] * prices[key]
    
print("Total value of available brands: ")

for key, value in total_value.items():
    print(key + ":", value) 

total = 0
for value in total_value.values():
    total += value
    
    
print("total value of available items:", total)





















































