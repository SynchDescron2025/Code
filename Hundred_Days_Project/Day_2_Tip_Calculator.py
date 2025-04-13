print("Welcome to Tip Calculator!")
bill = float(input("What is your total bill?"))
tip = int(input("How much tip would you like to give?"))
split = int(input("How many people will split the bill?"))
total = (bill + (bill*tip/100)) / split
print(f"You total is: {total:.2f}")
