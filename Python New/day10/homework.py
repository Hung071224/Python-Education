



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






























































































































