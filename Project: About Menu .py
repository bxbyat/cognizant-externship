def factorial(n: int):  # factorial function
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n: int):  # fibonacci function
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def menu():
    choice = input(
        "Welcome to the Recursive Artistry Program! Choose an option: 1. "
        "Calculate Factorial 2. Find Fibonacci 3. Exit > ")

    if int(choice) == 1:
        f = input("Enter a number to find its factorial: ")
        result = factorial(int(f))
        print("The factorial of " + str(f) + " is " + str(result) + ".")
    elif int(choice) == 2:
        f = input("Enter the position of the Fibonacci number: ")
        result = fibonacci(int(f))
        if f == 1:
            print("The 1st Fibonacci number is 1.")
        elif f == 2:
            print("The 2nd Fibonacci number is 1.")
        elif f == 3:
            print("The 3rd Fibonacci number is 2.")
        else:
            print("The " + f + "th Fibonacci number is " + str(result) + ".")
    elif int(choice) == 3:
        exit()
    else:
        print("Input is invalid!")


menu()