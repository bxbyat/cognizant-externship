# Task 1
name = "Hayley"
age = 21
height = 5.4

print("Hey there, my name is " + name + "! I’m " + str(age) + " years old and "
      + str(height) + " feet tall.\n")

# Task 2
num1 = 11
num2 = 5

print("The sum of 11 and 5 is", num1 + num2)  # addition
print("The difference between 11 and 5 is", num1 - num2)  # subtraction
print("The product of 11 and 5 is", num1 * num2)  # multiplication
print("The quotient of 11 and 5 is", num1 / num2, "\n")  # division


# Task 3
def number_checker():
    inp = input("Enter a number:")
    if float(inp) > 0:
        print("This number is positive. Awesome!")
    elif float(inp) < 0:
        print("This number is negative. Better luck next time!")
    else:
        print("Zero it is. A perfect balance!")


number_checker()