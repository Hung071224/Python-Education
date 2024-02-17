# Xây dựng lớp người dùng USER
class USER:
    # Khởi tạo các thuộc tính của lớp
    def __init__(self, fullname, email, birthday):
        self.fullname = fullname
        self.email = email
        self.birthday = birthday
    
    # Nhập các thuộc tính của người dùng từ bàn phím
    def input(self):
        self.fullname = input("Nhập họ tên đầy đủ: ")
        self.email = input("Nhập địa chỉ thư: ")
        self.birthday = input("Nhập ngày tháng năm sinh (dd/mm/yyyy): ")
    
    # Hiển thị thông tin của người dùng lên màn hình
    def display(self):
        print("Họ tên đầy đủ:", self.fullname)
        print("Địa chỉ thư:", self.email)
        print("Ngày tháng năm sinh:", self.birthday)
    
    # Tính tuổi của người dùng
    def age(self):
        from datetime import date
        today = date.today()
        day, month, year = map(int, self.birthday.split("/"))
        birthday = date(year, month, day)
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

# Xây dựng lớp tài khoản ACCOUNT kế thừa lớp USER
class ACCOUNT(USER):
    # Khởi tạo các thuộc tính của lớp
    def __init__(self, fullname, email, birthday, username, password):
        # Gọi phương thức khởi tạo của lớp cha
        super().__init__(fullname, email, birthday)
        self.username = username
        self.password = password
    
    # Đăng ký tài khoản với đầy đủ thông tin của người dùng
    def register(self):
        # Gọi phương thức nhập của lớp cha
        super().input()
        # Nhập tên người dùng và mật khẩu
        self.username = input("Nhập tên người dùng: ")
        self.password = input("Nhập mật khẩu: ")
        # Kiểm tra điều kiện hợp lệ
        valid = self.validate()
        # Nếu không hợp lệ, yêu cầu nhập lại
        while not valid:
            print("Tài khoản không hợp lệ, vui lòng nhập lại!")
            self.username = input("Nhập tên người dùng: ")
            self.password = input("Nhập mật khẩu: ")
            valid = self.validate()
        # Nếu hợp lệ, thông báo đăng ký thành công
        print("Đăng ký tài khoản thành công!")
    
    # Hiển thị thông tin tài khoản
    def display(self):
        # Gọi phương thức hiển thị của lớp cha
        super().display()
        # Hiển thị tên người dùng và mật khẩu
        print("Tên người dùng:", self.username)
        print("Mật khẩu:", self.password)
    
    # Hàm kiểm tra tài khoản có trùng username với một tài khoản khác hay không
    def is_duplicate(self, other):
        return self.username == other.username
    
    # Hàm kiểm tra tài khoản có hợp lệ hay không
    def validate(self):
        # Kiểm tra username không chứa kí tự trống
        if " " in self.username:
            return False
        # Kiểm tra mật khẩu gồm ít nhất 8 kí tự, bao gồm chữ hoa, chữ thường và kí tự số
        if len(self.password) < 8:
            return False
        has_upper = False
        has_lower = False
        has_digit = False
        for c in self.password:
            if c.isupper():
                has_upper = True
            if c.islower():
                has_lower = True
            if c.isdigit():
                has_digit = True
        return has_upper and has_lower and has_digit

# Nhập thông tin của n tài khoản từ bàn phím
n = int(input("Nhập số lượng tài khoản: "))
accounts = [] # Danh sách tài khoản
for i in range(n):
    print("Nhập thông tin tài khoản thứ", i + 1)
    account = ACCOUNT("", "", "", "", "") # Tạo đối tượng tài khoản
    account.register() # Đăng ký tài khoản
    accounts.append(account) # Thêm tài khoản vào danh sách

# Liệt kê danh sách các tài khoản của người dùng tiềm năng
print("Danh sách các tài khoản của người dùng tiềm năng:")
for account in accounts:
    if account.age() < 25: # Nếu tuổi nhỏ hơn 25
        account.display() # Hiển thị thông tin tài khoản
        print()

# Kiểm tra xem có hai tài khoản nào đó trùng tên người dùng hay không
duplicates = [] # Danh sách các tài khoản trùng lặp
for i in range(n):
    for j in range(i + 1, n):
        if accounts[i].is_duplicate(accounts[j]): # Nếu hai tài khoản trùng tên người dùng
            duplicates.append((i, j)) # Thêm cặp chỉ số vào danh sách
# Nếu có tài khoản trùng lặp
if duplicates:
    print("Có các tài khoản trùng tên người dùng sau:")
    # Liệt kê các tài khoản trùng lặp
    for i, (x, y) in enumerate(duplicates):
        print(i + 1, ".")
        print("Tài khoản thứ", x + 1)
        accounts[x].display()
        print("Tài khoản thứ", y + 1)
        accounts[y].display()
        print()
    # Yêu cầu người dùng chọn một tài khoản để xóa
    choice = int(input("Nhập số thứ tự của tài khoản bạn muốn xóa: "))
    # Lấy cặp chỉ số của tài khoản được chọn
    x, y = duplicates[choice - 1]
    # Xóa tài khoản khỏi danh sách
    accounts.pop(y)
    accounts.pop(x)
    # Cập nhật số lượng tài khoản
    n -= 2

# Hiển thị danh sách tài khoản sau khi loại bỏ tài khoản trùng lặp
print("Danh sách tài khoản sau khi loại bỏ tài khoản trùng lặp:")
for account in accounts:
    account.display()
    print()