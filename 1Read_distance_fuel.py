distance = float(input())
fuel = float(input())

if distance <= 0 and fuel <=0:
    print("Invalid Input")
else:
    milage = distance / fuel
    print(f"Milage:{milage}")