# for i in range(500):
#     print("Good morning, everyone!")


cars = ["Toyota", "Honda", "Ford", "BMW", "Tesla"]
for car in cars:
    print(car)

# range(stop)
# range(4)  --- > 0, 1, 2, 3
# range(start, stop)
# range(2, 5)  --- > 2, 3, 4
# range(start, stop, step)
# range(0, 10, -1)--- > 0, 2, 4, 6, 8

name = "Alice"
for char in name:
    print(char)

employees = [("Aisha",15000), ("Bob", 20000), ("Charlie", 18000)]
for name, salary in employees:
    monthly_salary = salary *22
    print(f"{name}'s monthly salary is Kshs.{monthly_salary}")