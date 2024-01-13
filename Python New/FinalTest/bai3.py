



def is_palindrome(string):
    reversed_string = string[::-1]
    if string== reversed_string:
        return True
    else:
        return False

string = input("Nhập một string: ")
if is_palindrome(string):
    print(string, "là 1 palindrome")
else:
    print(string, " không phải là 1 palindrome")
    


































