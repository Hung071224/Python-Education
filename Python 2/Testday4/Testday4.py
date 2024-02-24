








def separator(char, length):
    print(char * length)
class Book:
    def __init__(self, name, author, year, quantity):
        self.name = name
        self.author = author
        self.year = year
        self.quantity = quantity
    
    def display_info(self):
        separator ('-', 40)
        print("Tên sách:", self.name)
        print("Tác giả:", self.author)
        print("Năm sản xuất:", self.year)
        print("Số lượng:", self.quantity)
        separator ('-', 40)
        
class Library():
    def __init__(self):
        self.book = []
    
    def add_book(self,book1):
        self.book.append(book1)
    
    def display_all_book(self):
        for book1 in self.book:
            book1.display_info()
    
    def search_book(self, keyword):
        count = 0
        for book in self.book:
            if keyword.lower() in book.name.lower():
                count += 1
                book.display_info()
        
        if count == 0:
            print("Không có dữ liệu", keyword)
    
    def borrow_book(self, keyword, quantity):
        found = False
        for book in self.book:
            if keyword.lower() in book.name.lower():
                found == True
                
                if  book.quantity >= quantity:
                    book.quantity -= quantity
                    print("Bạn đã mượn thành công", quantity, "quyển", book.name)
                    
                else:
                    print("Số lượng sách", book.name, "Không đủ để mượn")
                break
            if not found: 
                print("Không có sách nào trong từ khóa", keyword)
    
    def return_book(self, keyword, quantity):
        found = False
        for book in self.book:
            if keyword.lower() in book.name.lower():
                found = True
                book.quantity += quantity
                print("Bạn đã trả thành công", quantity, "quyển", book.name)
                
                break
        if not found:
            print("Sách bạn muốn trả không phải của thư viện này")

separator ('=', 40)
library = Library()
separator ('=',40)
def display_menu():
    print("Chào mừng bạn đến với thư viện")
    separator ('=',40)
    print("Vui lòng chọn 1 trong các chức năng sau")
    separator ('=',40)
    print("1. ADD BOOK")
    separator ('=',40)
    print("2. Diplay All Books")
    separator ('=',40)
    print("3. Search Book")
    separator ('=',40)
    print("4. Borrow Book")
    separator ('=',40)
    print("5. Return Book")
    separator ('=',40)
    print("6. EXIT")
    separator ('=',40)
    
def input_book():
    name = input("Nhập tên sách: ")
    separator ('=',40)
    author = input("Nhập tên tác giả: ")
    separator ('=',40)
    year = int(input("Nhập năm sản xuất: "))
    separator ('=',40)
    quantity = int(input("Nhập sống lượng: "))
    separator ('=',40)
    
    return Book(name, author, year, quantity)

def run_program():
    while True:
        display_menu()
        choice = int(input("Nhập lựa chọn của bạn: "))
        if choice == 1:
            book = input_book()
            library.add_book(book)
            print("Đã thêm sách thành công")
            
        elif choice == 2:
            separator ('=',40)
            library.display_all_book()
        
        elif choice == 3:
            separator ('-', 40)
            keyword = input("Nhập tên sách cần mượn: ")
            library.search_book(keyword)
            separator ('-', 40)
        elif choice == 4:
            separator ('-', 40)
            keyword = input("Nhập tên sách cần mượn: ")
            quantity = int(input("Nhập số lượng: "))
            library.borrow_book(keyword, quantity)
            separator ('-', 40)
        elif choice == 5:    
            separator ('*', 40)
            keyword = input("Nhập tên sách đã mượn: ")
            quantity = int(input("Nhập số lượng: "))
            library.return_book(keyword, quantity)
            separator ('*', 40)
        elif choice == 6:
            separator ('*', 40)
            print("Cảm ơn bạn đã sử dụng thư viện")
            separator ('*', 40)
            break
        else:
            print("Lựa chọn không hợp lẹ. Vui lòng nhập lại")
run_program()





































