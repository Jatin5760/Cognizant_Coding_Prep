Salary = float(input("Enter your salary: "))
Total_Salary = 0;

if Salary <= 0:
    print("Invalid input")
    
Total_Salary = Salary + (0.20 * Salary) + (0.10 * Salary) - (0.12 * Salary)
print(f"Your total salary after process is = {Total_Salary:.5f}")