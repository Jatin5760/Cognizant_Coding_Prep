Units = float(input("Enter the units consumed: "))
Bill= 0

if Units <=0:
    print("Invalid Input")
    
elif Units <= 100:
    Bill = Units * 1.5
    
elif Units >=101 and Units <= 200:
    Bill = 100 * 1.5 + (Units - 100) * 2.0
    
elif Units > 200:
    Bill = (100 * 1.5) + (100 * 2.0) + ((Units - 200) * 3.0)
    
print(f"Your total Bill Amount is =  {Bill}")