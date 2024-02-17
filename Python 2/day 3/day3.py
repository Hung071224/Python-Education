








class USER: 
    def _init_(self, fullname, email, birthday):
        self.fullname = fullname
        self.email = email
        self.birthday = birthday
        
    def input(self):
        self.fullname = input("Nhập họ tên đầy đủ: ")
        self.email = input("Nhập địa chỉ email: ")
        self.birthday = input("Nhập ngày tháng năm sinh (đ/mm/yyyy): ")\
    
    def display(self):
        print("Họ tên đầy đủ: ", self.fullname)
        print("Địa chỉ email: ", self.email)
        print("Ngày tháng năm sinh: ", self.birthday)
    
    def age(self):
        from datetime import date
        today = date.today()
        day, month, year = map(int, self.birthday.split("/"))
        birthday = date(year, month, day)
        return today.year - birthday.year - ((today.month,today.day)<(birthday.month,birthday.day))

class ACCOUNT(USER):
    def _init_(self, fullname, email, birthday, username, password):
        super().init_(fullname, email, birthday)
        self.username = username
        self.password = password
        
    def register(self):
        super().input()
        self.username= input("Nhập tên người dùng: ")
        self.password= input("Đặt mật khẩu: ")
        valid = self.validate()
        while not valid:
            print("Tài khoản không hợp lệ, vui lòng nhập lại!")
            self.username= input("Nhập tên người dùng: ")
            self.password= input("Đặt mật khẩu: ")
            valid = self.validate()
            
        print("Đăng ký tài khoản thành công: ")
    
    def display(self):
        super().display()
        print("Tên người dùng: ", self.username)
        print("Mật khẩu: ", self.password)
        
    def duplicate(self, other):
        return self.username == other.username
    
    def validate(self):
        if " " in self.username:
            return False
        
        if len(self.password) < 8:
            return False
        has_upper = False
        has_lower = False
        has_digit = False
        for c in self .password:
            if c.isupper():
                has_upper = True
            if c.islower():
                has_lower = True
            if c.isdigit():
                has_digit = True
        return has_upper and has_lower and has_digit
    
n = int(input("Nhập số lượng tài khoản: "))
accounts = []
for i in range(n):
    print("Nhập thông tin tài khoản thứ", i + 1)
    account = ACCOUNT("", "", "", "", "")
    account.register()
    accounts.append(account)
        
print("Danh sách tài khoản tiềm năng: ")
for account in accounts:
    if account.age()<25:
        account.display()
        print()
    
duplicates = []
for i in range(n):
    for j in range(i + 1, n):
        if accounts[i].is_duplicate(accounts[j]):
            duplicates.append((i,j))
if duplicates:
    print("Có các tài khoản trùng tên người dùng sau: ")
    for i, (x, y) in enumerate(duplicates):
        print(i + 1, ".")
        print("Tài khoản thứ", x + 1)
        accounts[x].display()
        print("Tài khoản thứ", y + 1)
        accounts[y].display()
        print()
    choice = int(input("Nhập số thứ tự của tài khoản bạn muốn xóa: "))
    x, y = duplicates[choice - 1]
    accounts.pop(y)
    accounts.pop(x)
    n -= 2

print("Danh sách tài khoản sau khi loại bỏ tài khoản trùng lặp:")
for account in accounts:
    account.display()
    print()

        
    
        

        
        
    
    
        
        
        
        














































































