# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered, changeable and does not allow duplicates.

# Create and print a dictionary:
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "phone": "123-456-7890"
}
print(person)

# Accessing values in a dictionary:
print(person["name"])  # Access value by key
print(person["age"])   # Access value by key
print(person["city"])  # Access value by key
print(person["phone"]) # Access value by key

# Adding a new key-value pair to the dictionary:
person["email"] = "john@example.com"
print(person)