# Task 1
s = "Python is amazing!"

print("First word: " + s[0:6])
print("Amazing part: " + s[10:17])
print("Reversed string: " + s[::-1])

# Task 2
s = " hello, python world! "
print(s)

s = s.strip()
print(s)

s = s.capitalize()
print(s)

s = s.replace("world", "universe")
print(s)

s = s.upper()
print(s)


# Task 3
def palindrome():
    word = input("Enter a word: ")
    compare = word[::-1]
    if word == compare:
        print("Yes, '", word, "' is a palindrome!")
    else:
        print("No, '", word, "' is not a palindrome.")