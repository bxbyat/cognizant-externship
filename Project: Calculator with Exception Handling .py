def calculator():
    print("Welcome to the Error-Free Calculator!")
    op = input("Choose an operation: 1. Addition 2. Subtraction "
               "3. Multiplication 4. Division 5. Exit > ")
    try:
        int(op) in [1, 2, 3, 4, 5]
    except ValueError:
        print("Invalid input! Please enter a valid number. ")
    else:
        while True:
            try:
                num1 = int(input("Enter the first number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number. ")
            else:
                break
        while True:
            if int(op) == 4:
                try:
                    num2 = int(input("Enter the second number: "))
                    test = num1 / num2
                except ValueError:
                    print("Invalid input! Please enter a valid number. ")
                except ZeroDivisionError:
                    print("Oops! Division by zero is not allowed.")
                else:
                    break
            else:
                try:
                    num2 = int(input("Enter the second number: "))
                except ValueError:
                    print("Invalid input! Please enter a valid number. ")
                else:
                    break
        if int(op) == 1:
            print("The sum of " + str(num1) + " and " + str(num2) + " is " +
                  str(num1 + num2) + ".")
        elif int(op) == 2:
            print("The difference between " + str(num1) + " and " + str(num2)
                  + " is " + str(num1 - num2) + ".")
        elif int(op) == 3:
            print("The product of " + str(num1) + " and " + str(num2) + " is "
                  + str(num1 * num2) + ".")
        elif int(op) == 4:
            print("The quotient of " + str(num1) + " and " + str(num2) + " is "
                  + str(num1 / num2) + ".")
        elif int(op) == 5:
            exit()
    finally:
        print("Thanks for using this calculator! :)")


calculator()