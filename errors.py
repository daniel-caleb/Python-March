# Types of Errors in Python

# 1. Syntax Errors: These occur when the code is not written in the correct syntax. For example:
print("Hello, World!")  # Missing closing parenthesis

# 2. Name Errors: These occur when you try to use a variable or function that has not been defined. For example:
x= 10
print(x)  # x is not defined

# 3. Type Errors: These occur when you try to perform an operation on incompatible data types. For example:

result = "Hello" + "5"  # Cannot concatenate string and integer

# 4. Value Errors: These occur when a function receives an argument of the correct type but an inappropriate value. For example:
# int("abc")  # Cannot convert string to integer

# 5. Index Errors: These occur when you try to access an index that is out of range in a list or string. For example:
my_list = [1, 2, 3]
print(my_list[2])  # Index out of range

# 6. Key Errors: These occur when you try to access a key that does not exist in a dictionary. For example:
my_dict = {"name": "Alice", "age": 30, "gender":"Female"}
print(my_dict["gender"])  # KeyError: 'gender not found in dictionary'

# Zero Division Errors: These occur when you try to divide a number by zero. For example:
result = 10 / 0  # ZeroDivisionError: division by zero