

"""

def fibonacci(n):
    if n <= 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("enter a positive integer: "))
print(f"The number of pairs of rabbit in {n} months is {fibonacci(n)}")


"""



#cách 1: need help 

"""

a = int(input("Nhập tử số: "))
b = int(input("Nhập mẫu số: "))
u = math.gcd(a, b)
p = a // u
q = b // u 
print ("phân số rút gọn là: ", p, "/", q)


"""



#cách 2

a = int(input("Nhập tử số: "))
b = int(input("Nhập mẫu số: "))
u = a
v = b
q = a%v
r = b%v
while u !=0 or v !=0:
    if u == 0:
        print("Phân số rút gọn là: ", q, "/", r)
        break
    elif v == 0 :
        print("Phân số rút gọn là: ", q, "/", r)
        break
    if q % r !=0:
        print("Phân số rút gọn là: ", q, "/", r)
        if u > v:
            u -= q*r
        else:
            v-= q*r
    q= a % v
    r= b % v
if u !=0 or v !=0:
    print("Phân số rút gọn là: ", q, "/", r)


























































