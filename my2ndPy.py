if 1 + 1 == 3:
    print("All these statements")
    print("sharing the same indentation")

    print("will execute when the condition evaluates true")
print("This statement does not belong to the conditional and will always execute")

mix = [1, 'cat', ['list', 'in', 'a', 'list'], {'name' : 'matt', 'age' : 30}]
for item in mix:
    print(item)

numbers = [1, 20, 3, 40, 5, 60, 7, 80, 9]
for n in range(2, len(numbers), 2):  # Starts at 2, less than the length of the list (in this case 9), step by 2
    print(numbers[n])