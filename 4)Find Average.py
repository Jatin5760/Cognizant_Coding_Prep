num1 = int(input("Enter 1st numbers"))
num2 = int(input("Enter 2nd numbers"))
num3 = int(input("Enter 3rd numbers"))


if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("Invalid Input")
else:
    avg = (num1 + num2 + num3) / 3
    print(f"Average = {avg:.2f}")


