correct_pin = "1234"
attempts = 0

while attempts < 3:
    entered_pin = input("Please enter your PIN: ")
    
    if entered_pin == correct_pin:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {3 - attempts} attempts left.")

if attempts == 3:
    print("Too many incorrect attempts. Access denied.")