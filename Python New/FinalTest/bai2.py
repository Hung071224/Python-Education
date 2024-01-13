



a = float(input( "Nhập Hệ số a(Khác 0):"))

b = float(input( "Nhập Hệ số b: "))

c = float(input( "Nhập Hệ số c: "))

delta = b**2 - 4*a*c
if delta < 0:
    print("invalid delta")
elif delta == 0:
    x = -b/(2*a)
    print("Phương trình có nghiệm kép x =", x)
else:
    x1 = (-b + delta**0.5)/ (2*a)
    x2 = (-b - delta**0.5)/ (2*a)
    print("Phương trình có 2 nghiệm phân biệt x1 = ", x1, "và x2= ",x2)


































