cars = ["Toyota", "Honda", "Ford", "BMW", "Tesla", "Mercedes", "Audi", "Nissan", "Hyundai", "Kia"]

for car in cars:
    if car == "Nissan":
        print("Found the car, breaking out of the loop.")
        break
    print(f"Checking car: {car}")
print("Loop has ended.")