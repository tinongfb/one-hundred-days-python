print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

calculated_tip = bill + (bill * (tip/100))
split_bill = (calculated_tip / people)
rounded_bill = round(split_bill, 2)
print(f"Each person should pay: ${rounded_bill}")