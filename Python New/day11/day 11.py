



fh = open("C:\\Users\\PC\\Python Education\\Python New\\day11\\test.txt" , "r")


"""
print (fh)

"""

"""
for line in fh:
    print(line)

"""


lst = []
for line in fh:
    line = line.replace("\n", "")
    lst.append(line)
lst
















