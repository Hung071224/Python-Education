


"""




class DragonBall:
    def __init__(self, name, level, hair, power):
        self.name = name
        self.level = level
        self.hair = hair
        self.power = power
        
    def level_up(self):
        self.level += 1
        self.power += 1000
        print(f"Level Up!!!!!")
    
    def reset(self):
        self.level = 1
        self.power = 10
        self.hair = "black"
        print(f"Reset!!!")
        
    def super_saiyan(self, number, hair_color):
        self.level += (number * 10)
        self.hair = hair_color
        self.power *= number
        print(f"SUPER SAIYAN!!!!!")
    
    def show(self):
        print(f"Name: {self.name} ,Level: {self.level},Hair: {self.hair},Powers: {self.power}")

                      



chap1 = DragonBall("Goku", 1, "black", 1000)
chap1.show()
chap1.level_up()
chap1.show()

"""





class Person:
    def __init__(self, cmt, ho_ten, nam_sinh, gioi_tinh, que_quan):
        self.cmt = cmt
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.que_quan = que_quan
        
    def nhap(self):
        self.cmt = int(input("Nhập CMT/CCCD: "))
        self.ho_ten = input("Nhập họ và tên: ")
        self.nam_sinh =int(input("Nhập năm sinh: "))
        self.gioi_tinh = input("Nhập giới tính: ")
        self.que_quan = input("Nhập quên quán: ")
    
    def hien_thi(self):
        print("CMT/CCCD: ", self.cmt)
        print("Năm sinh: ", self.nam_sinh)
        print("Giới tính: ", self.gioi_tinh)
        print("Quê quán: ", self.que_quan)

class Student(Person):
    def __init__(self, cmt, ho_ten, nam_sinh, gioi_tinh, que_quan, ma_sv, diem_gk, diem_ck):
        super().__init__(cmt, ho_ten, nam_sinh, gioi_tinh, que_quan)
        self.ma_sv = ma_sv
        self.diem_gk = diem_gk
        self.diem_ck = diem_ck

    def nhap(self):
        super().nhap()
        self.ma_sv = input("Nhập mã SV: ")
        self.diem_gk = float(input("Nhập điểm giữa kì: "))
        self.diem_ck = float(input("Nhập điểm cuối kì: "))

    def hien_thi(self):
        super().hien_thi()
        print("Mã SV:", self.ma_sv)
        print("Điểm giữa kì:", self.diem_gk)
        print("Điểm cuối kì:", self.diem_ck)
        print("Điểm trung bình:", self.tinh_dtb())

    def tinh_dtb(self):
        return (self.diem_gk + self.diem_ck * 2) / 3

danh_sach = []
for i in range (3):
    print(" Nhập dữ liệu cho sinh viên thứ: ", i + 1)
    sv = Student("", "", 0, "", "", "", 0.0, 0.0)
    sv.nhap()
    danh_sach.append(sv)

for i in range(3):
    print("Dữ liệu của sinh viên thứ:", i + 1)

danh_sach[i].hien_thi()
danh_sach.sort(key=lambda sv: sv.tinh_dtb(), reverse=True)

print("Thứ tự xếp hạng theo điểm trung bình: ")
for i in  range (3):
    print("Hạng", i + 1, ":", danh_sach[i].ho_ten, "với điểm trung bình là: ", danh_sach[i].tinh_dtb())










































