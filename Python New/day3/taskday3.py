#bài 1
"""


n = int(input("nhập n từ bàn phím"))
sum = 0
for i in range (1, n+1):
    if i % 2 ==0:sum += i
print("tổng các số chẵn từ 1 đến",n,"là",sum)


"""



#bài 2

"""
n = int(input("nhập n từ bàn phím"))
print("Các ước số của",n,"là")
for i in range (1, n+1):
    if n % i == 0:
        print (i)

"""





#bài 3
"""

n = int(input("nhập n từ bàn phím"))
is_prime = True
if n <2:
    is_prime = False 
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
            is_prime = False 
            break
if is_prime: print(n, "là số nguyên tố") 
else: print(n, "không phải số nguyên tố")

"""
