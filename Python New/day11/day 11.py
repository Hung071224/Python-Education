



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




















"""

with open("C:\\Users\\PC\\Python Education\\Python New\\day11\\vanban.txt", "r") as f:
    data = f.read()
    words = data.split()
    num_words = len(words)
    print("Số từ trong file là: ", num_words)
    
"""




with open("C:\\Users\\PC\\Python Education\\Python New\\day11\\dayso.txxt", "r") as f:
    count ={}
    for line in f:
        numbers = [int(x) for x in line.split()]
        for num in numbers:
            if num in count:
                count[num] += 1
            else:
                count[num] =1
    print("Có", len(count), "Số Nguyên khác nhau trong file")
    for num, freq in count.items():
        print("Số", num,"xuất hiện", freq, "lần") 
































































