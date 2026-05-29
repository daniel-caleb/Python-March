names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names)
print(names[0])  # First element
print(names[1])  # Second element

names.append("Frank")  # Add a new name to the list
print(names)
names.remove("Charlie")  # Remove a name from the list
print(names)

print(len(names))  # Print the length of the list

mixed_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(mixed_list)