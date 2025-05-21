# Task 1
fruits = ["mango", "orange", "pear", "pineapple", "strawberry"]
print("Original list: ", fruits)

fruits.append("banana")
print("After adding a fruit: ", fruits)

fruits.remove("pineapple")
print("After removing a fruit: ", fruits)

print("Reversed list: ", fruits[::-1])

# Task 2
info = {"name": "Lola", "age": "21", "city": "New York"}
info.update({"favorite color": "pink"})
info["city"] = "Dubai"
print("Keys:")
for i in info:
    print(i)
print("Values:")
for i in info:
    print(info[i])

# Task 3
faves = ("The Book of Life", "Born to Die", "The Song of Achilles")
# faves[1] = "Dark Paradise"
print("Length of tuple: ", len(faves))