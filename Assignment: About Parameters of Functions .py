# Task 1
def greet_user(name: str):
    return "Hello, " + name + "! Welcome aboard."


print(greet_user("Lola"))


def add_numbers(x: float, y: float):
    return "The sum of " + str(x) + " and " + str(y) + " is " + str(x + y) + "."


print(add_numbers(12, 4))


# Task 2
def describe_pet(pet_name: str, animal_type="dog"):
    return "I have a " + animal_type + " named " + pet_name + "."


print(describe_pet("Buddy"))
print(describe_pet("Luna", "cat"))


# Task 3
def make_sandwich(*ingredients):
    sandwich = "Making a sandwich with the following ingredients: "
    for i in ingredients:
        sandwich += "- " + i + " "
    return sandwich


print(make_sandwich("lettuce", "tomato", "chicken"))
print(make_sandwich("cheese", "cucumber"))


# Task 4
def factorial(n : int):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
print(factorial(4))
print(factorial(5))


def fibonacci(n: int):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
print(fibonacci(7))