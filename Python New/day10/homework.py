



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



























































































































