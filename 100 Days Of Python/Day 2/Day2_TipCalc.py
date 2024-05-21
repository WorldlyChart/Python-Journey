#Tip calculator
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? \n$"))
tip = 1 +.01 * float(input("What percentage would you like to tip?(no percent signs) \n"))
split = int(input("How many people are splitting the bill? \n"))
per_person = total * tip / split
per_person_round = "{:.2f}".format(per_person)
print(f"Each person should pay: ${per_person_round}")