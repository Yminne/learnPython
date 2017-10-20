groceryDict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}

for item, price in groceryDict.items():
    print("Item: %s, cost: %4.2f" % (item, price))

groceryDict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}
groceryDict.pop("eggs")        # Removes eggs from the dictionary
groceryDict["bananas"] = 2.33  # Add new item to dictionary

for item, price in groceryDict.items():
    print("Item: %s cost: %4.2f" % (item, price))

a = {}
a["a"] = "A"
a[65] = "A"
print(a)