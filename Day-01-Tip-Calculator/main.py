print("=== Welcome to our bill calculator! ===")

total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? %"))
people = int(input("How many people to split the bill? "))

tip_multiplier = 1 + (tip_percent / 100)
bill_per_person = (total_bill / people) * tip_multiplier

print(f"Each person should pay: ${bill_per_person:.2f}")
