

"""

def fibonacci(n):
    if n <= 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("enter a positive integer: "))
print(f"The number of pairs of rabbit in {n} months is {fibonacci(n)}")

"""












































































