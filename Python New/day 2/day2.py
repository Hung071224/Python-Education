"""

a= "this is a"
b= "string"
print (a + b * 3)


"""



#len la ham lay do dai cua xau
"""


name = "Nguyen Minh Hung"
l=len(name)
print (f"length string: {l}")

    

"""


"""



#cu phap cat xau: name_string[start : end : step]
#vi tri dau tien cua xau --> luon luon la 0
name = "Nguyen Minh Hung"
lname= name[7:12:1]
m_name = name [: 7 ] 
f_name = name [12:]
print (m_name)
print (lname)
print (f_name)



"""




"""



# step (cach don vi)
s="0123456789123456789"
x= s[1::2]   #x= s[1::-1]
print (x)    #vị trí cuối cùng của 1 xâu: -1

#(-1) ngược lại


"""



"""



#chuẩn hóa xâu --> biến xâu về 1 dạng theo quy chuẩn
name = "Nguyễn Minh Hùng"
name_lower = name.lower ()
name_upper = name.upper ()
name_titles = name.title()
print (name_lower)
print (name_upper)
print (name_titles)



"""


















"""


#kiểm tra kiểu cỉa biến : type()
number = 3.14
print (type(number))


"""






"""
#bool "true - false"
check = True
check = False
check = 5 <= 3
print(type(check))
print(check)

"""



"""


#Cú pháp câu rệnh rẽ nhánh

# ìf biểu thức điểu kiện :
#            <thực hiện code nếu btđk đúng>


a= 5
b=6
if a == b:
    print ("a và b bằng nhau")
else:
    print ("a không bằng b và bé hơn b")


"""

"""


#kiểm tra tiếp


a= 5
b=6
if a == b:
    print ("a và b bằng nhau")
else:
    if a <= b:
        print ("a nhỏ hơn b")
    else:
        print("a không bé hơn b")


"""



"""


a = int(input("nhập vào 1 số nguyên bất kỳ"))
if a>0:
    print ("a là số nguyên dương")
else:
    print ("a là số nguyên âm")

if a%2!=0:
    print ("a là số lẻ")
else:
    print ("a là số chẵn")

       
"""       




"""


a = float(input("nhập 1 số bất kỳ"))
b = float(input("nhập 1 số bất kỳ"))
c = float(input("nhập 1 số bất kỳ"))

min = a
if min<b:
    min = b
if min>c:
    min=c
print (f"số nhỏ nhất là: {min}")


"""




###issue 

month = int(input("what is the month?"))
year = int(input("what is the year?"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print ("this month have 31 days")
else:
    if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
        print ("this month have 30 days")
    
    if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
           print ("This month in this {year} have 29 days")

 


















































