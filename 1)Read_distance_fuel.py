distance = float(input("Enter the total distance travelled in (KM): "))
fuel = float(input("Enter the fuel consumed in (L): "))

if distance <= 0 or fuel <=0:
    print("Invalid Input")
else:
    milage = distance / fuel
    print(f"Your car's Milage :{milage}")