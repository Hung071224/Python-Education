

# Python 

count = 0

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def is_missing(x, y, n):
    if n == 2:
        return (x == 0 and y == 1)
    half = n // 2
    if x < half and y < half:
        return False
    elif x < half and y >= half:
        return is_missing(x, y - half, half)
    elif x >= half and y < half:
        return False
    else:
        return False

def lat_nen(matrix, x, y, n):
    global count 
    if n == 2:
        count += 1
        for i in range(x, x + n):
            for j in range(y, y + n):
                if not is_missing(i, j, n):
                    matrix[i][j] = count
        return
    half = n // 2
    lat_nen(matrix, x, y, half)
    lat_nen(matrix, x, y + half, half)
    lat_nen(matrix, x + half, y, half)
    lat_nen(matrix, x + half, y + half, half)
    count += 1 
    for i in range(x + half - 1, x + half + 1):
        for j in range(y + half - 1, y + half + 1):
            if not is_missing(i, j, n):
                matrix[i][j] = count

def main():
    k = int(input("Nhap k (2 <= k <= 10): "))
    if k < 2 or k > 10:
        print("k khong hop le!")
        return
    n = 2 ** k
    matrix = [[0] * n for _ in range(n)]
    lat_nen(matrix, 0, 0, n)
    print("So vien gach hinh tho can dung la:", count)
    print("Ma tran ket qua la:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()



#true false

count = 0

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def is_missing(x, y, n):
    if n == 2:
        return (x == 0 and y == 1)
    half = n // 2
    if x < half and y < half:
        return False
    elif x < half and y >= half:
        return is_missing(x, y - half, half)
    elif x >= half and y < half:
        return False
    else:
        return False

def lat_nen(matrix, x, y, n):
    global count
    if n == 2:
        count += 1
        for i in range(x, x + n):
            for j in range(y, y + n):
                if not is_missing(i, j, n):
                    matrix[i][j] = True
        return
    half = n // 2
    lat_nen(matrix, x, y, half)
    lat_nen(matrix, x, y + half, half)
    lat_nen(matrix, x + half, y, half)
    lat_nen(matrix, x + half, y + half, half)
    count += 1 
    for i in range(x + half - 1, x + half + 1):
        for j in range(y + half - 1, y + half + 1):
            if not is_missing(i, j, n):
                matrix[i][j] = True

def main():
    k = int(input("Nhap k (2 <= k <= 10): "))
    if k < 2 or k > 10:
        print("k khong hop le!")
        return
    n = 2 ** k
    matrix = [[False] * n for _ in range(n)]
    lat_nen(matrix, 0, 0, n)
    print("So vien gach hinh tho can dung la:", count)
    print("Ma tran ket qua la:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()





















