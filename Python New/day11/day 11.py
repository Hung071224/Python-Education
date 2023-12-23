



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


"""


file = open("C:\\Users\\PC\\Python Education\\Python New\\day11\\vanban,inp", "r")
so_chu_thuong = 0
so_chu_hoa = 0
so_chu_so = 0
so_ki_tu_dac_biet = 0
for dong in file:
    for ki_tu in dong:
        if ki_tu.islower():
            so_chu_thuong += 1 
        elif ki_tu.isupper():
            so_chu_hoa += 1
        elif ki_tu.isdigit():
            so_chu_so += 1
        else: 
            so_ki_tu_dac_biet += 1
file.close()
file = open("C:\\Users\\PC\\Python Education\\Python New\\day11\\vanban.out", "w")
file.write(f"{so_chu_thuong} {so_chu_hoa} {so_chu_so} {so_ki_tu_dac_biet}\n")
file.close()



























































