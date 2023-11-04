#BÀI  1





n = int(input("nhập số nguyên n:"))

x = int(input("nhập số nguyên x:"))

numbers = []
for i in range (n):
    num = int(input(f"nhập số thứ {n+1}: "))
    numbers.append(num)

sum=0

for num in numbers :
    if num % x == 0 :
       sum += num
print (f"Tổng các số chia hết cho {x} là: {sum}") 






































# bài 2




m = int(input("nhập số nguyên m: "))

n= int(input("nhập số nguyên n: "))

matrix = []
for i in range (m):
    row = input(f"Nhập dòng thứ {i + 1}: ")
    row = [int(x) for x in row.split()]
    matrix.append(row)
transpose = []

for j in range (n):
    row = []
    for i in range(m):
        element = matrix[i][j]
        
    row.append(element)
    transpose.append(row)
    
print("Ma trận hoán vị của ma trận vừa nhập là: ")
for row in transpose:
    print(*row)








# bài 3 




n = int(input("Nhập số loại nấm n: "))

nutrition = []
toxin = []

for i in range(n):
    a, b = map(float,input (f"Nhập mức dinh dưỡng và lượng độc tố của loại nấm thứ {i+1}").split())
    nutrition.append(a)
    toxin.append(b)
    
edible = []
for i in range(n):
    if nutrition[i] >= 2 * toxin[i]:
        edible.append(i)
print("các loại nấm mà người dân có thể hái về ăn được là: ")
for i in edible:
    print(f"Loại nấm thyws {i+1}: mức dinh dưỡng là {nutrition[i]}, lượng độc tố là {toxin[i]}")


max_toxin = []
most_toxic = []

for i in range(n):
    if toxin[i] == max_toxin:
        most_toxic.append(i)

print(f" các Loại nấm thứ có độc tố cao nhất là: ")
for i in most_toxic:
    print (f"Loại nấm thứ {i+1}: mức dinh dưỡng là {nutrition[i]}, lượng độc là {toxin[i]}")

for i in range(n-1):
    min_index = i
    for j in range (i+1,n):
        if nutrition[j] < nutrition[min_index]:
            min_index = j
    nutrition[i],nutrition[min_index] = nutrition[min_index], nutrition[i]
    toxin[i],
toxin[min_index] = toxin[min_index], toxin[i]


print ("Các loại nấm sau khi sắp xếp theo chiều không giảm của mức dinh dưỡng là: ")
for i in range(n):
    print (f"Loại nấm thứ {i+1}: mức dinh dưỡng là {nutrition[i]}, lượng độc tố là {toxin[i]}")







