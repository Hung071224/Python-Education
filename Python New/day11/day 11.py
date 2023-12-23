



"""


fh = open("C:\\Users\\PC\\Python Education\\Python New\\day11\\test.txt" , "r")
print (fh)
for line in fh:
    print(line)
lst = []
for line in fh:
    line = line.replace("\n", "")
    lst.append(line)
lst


"""






















with open("C:\\Users\\PC\\Python Education\\Python New\\day11\\vanban.txt", "r") as f:
    data = f.read()
    words = data.split()
    num_words = len(words)
    print("Số từ trong file là: ", num_words)
    






































































