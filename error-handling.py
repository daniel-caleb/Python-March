try:
    # Attempt to perform a division by zero, which will raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the exception and print an error message
    print("Error: Cannot divide by zero. Please provide a non-zero denominator.")
    print("Exception details:", e)

print("This line will still execute, demonstrating that the program continues after handling the error.")