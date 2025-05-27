# Step 1
print("Welcome to the Inventory Manager!")
print("Current inventory:")
inventory = {"apple": (10, 2.5), "banana": (20, 1.2)}

for i in inventory:
    print("Item:", i, ", Quantity:", inventory[i][0], ", Price: $", inventory[i][1])

# Step 2
inventory["mango"] = (15, 3.0)
print("Adding a new item: mango")
inventory.pop("apple")
inventory["banana"] = (25, 1.2)

# Step 3
print("Updated inventory:")
for i in inventory:
    print("Item:", i, ", Quantity:", inventory[i][0], ", Price: $", inventory[i][1])

# Step 4
total = 0
for i in inventory:
    total += inventory[i][0] * inventory[i][1]
print("Total value of inventory: $", total)