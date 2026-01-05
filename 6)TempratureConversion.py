temp = float(input())

if temp < -273.15:
    print("Invalid Input")
else:
    fahrenheit  = (temp * 9/5) + 32
    print(f"Fahrenheit = {fahrenheit:.2f}")