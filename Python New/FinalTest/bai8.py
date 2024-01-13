

n = int(input('Nhập vào số n>0: '))
if n <= 0:
    print("Số bạn nhập không hợp lệ. ")
if n == 1:
    print('Số fibonacci đầu tiên là: 1')
elif n == 2:
    print('Sô fibonacci thứ 2 là: 1 1')
else:
    print(f'Số Fibonacci đầu tiên {n}: 1 1',end = ' ')
    f1 = 1
    f2 = 1
    fn = 0
    for i in range(3,n+1):
        fn = f1 + f2
        print(fn,end = ' ')
        f1 = f2
        f2 = fn





































