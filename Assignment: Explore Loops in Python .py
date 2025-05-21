# Task 1
def countdown():
    start = int(input("Enter the starting number: "))
    while start > 0:
        print(start)
        start -= 1
    print("Blast off! 🚀\n")


# Task 2
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


# Task 3
def find_factorial():
    num = int(input("Enter a number: "))
    result = 1
    for i in range(1, num + 1):
        result *= i
    print("The factorial of", num, "is", result, ".")