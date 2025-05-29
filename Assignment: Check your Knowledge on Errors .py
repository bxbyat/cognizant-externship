# Task 1
def divide_by():
    try:
        num = int(input("Enter a number: "))
        result = round(100 / num, 2)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    else:
        print("100 divided by " + str(num) + " is " + str(result))


# divide_by()


# Task 2
def access_index(i: int, values: list):
    if i < 0 or i >= len(values):
        raise IndexError("IndexError occurred! List index out of range.")


# access_index(4, [1, 2, 3])


def check_key(key: str, d: dict):
    if key not in d:
        raise KeyError("KeyError occurred! Key not found in the dictionary.")


# check_key("p", {"a": 0, "b": 4, "c": 1})


def add_two(a, b):
    if type(a) != type(b):
        raise TypeError("TypeError occurred! Unsupported operand types.")


# add_two("a", 1)


# Task 3
def divide():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try:
        result = round(int(num1) / int(num2), 4)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    else:
        print("The result is " + str(result) + ".")
    finally:
        print("Thanks for using this program.")


divide()