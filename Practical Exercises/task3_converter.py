print('Unit Converter')
print('1. Kilometres to Miles')
print('2. Kilograms to Pounds')
print('3. Celsius to Fahrenheit')

choice = input('Choose a conversion (1/2/3): ')

if choice == '1':
    km = float(input('Enter kilometres: '))
    miles = km * 0.621371
    print(f'{km} km = {miles:.2f} miles')

elif choice == '2':
    kg = float(input('Enter kilograms: '))
    pounds = kg * 2.20462
    print(f'{kg} kg = {pounds:.2f} pounds')

elif choice == '3':
    celsius = float(input('Enter Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}°C = {fahrenheit:.2f}°F')

else:
    print('Invalid choice. Please enter 1, 2, or 3.')











































































# Created by d4ktari on 2026-06-02