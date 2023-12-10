



#bài 1


def ucln(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def rut_gon(a, b):
  u = ucln(a, b)
  a = a // u
  b = b // u
  return (a, b)

a = int(input("Nhập tử số: "))
b = int(input("Nhập mẫu số: "))

a, b = rut_gon(a, b)

print("Dạng rút gọn của phân số là: {}/{}".format(a, b))





#bài 2



def tong_uoc(n):
  tong = 0
  for i in range(1, n + 1):
    if n % i == 0:
      tong = tong + i
  return tong

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

tong_x = tong_uoc(x)
tong_y = tong_uoc(y)
tong_xy = tong_x + tong_y

print("Tổng các ước của x là: {}".format(tong_x))
print("Tổng các ước của y là: {}".format(tong_y))
print("Tổng các ước của x và y là: {}".format(tong_xy))





#bài 3

def la_so_nguyen_to(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def tong_so_nguyen_to(n):
  tong = 0
  for i in range(1, n + 1):
    if la_so_nguyen_to(i):
      tong = tong + i
  return tong

n = int(input("Nhập n: "))

tong = tong_so_nguyen_to(n)

print("Tổng các số nguyên tố từ 1 đến {} là: {}".format(n, tong))




#bài 4



def la_so_nguyen_to(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def la_so_mersen(M):
  n = 2
  while True:
    x = 2 ** n - 1
    if M == x:
      if la_so_nguyen_to(M) and la_so_nguyen_to(n):
        return True
      else:
        return False
    elif M < x:
      return False
    n = n + 1

P = int(input("Nhập P: "))

if la_so_mersen(P):
  print("P là số Mersen")
else:
  print("P không phải là số Mersen")











#bài 5


def dec_to_bin(n):
  result = ""
  while n > 0:
    remainder = n % 2
    result = str(remainder) + result
    n = n // 2
  return result

n = int(input("Nhập một số nguyên dương: "))

binary = dec_to_bin(n)

print("Số nhị phân tương ứng là: {}".format(binary))



































































































