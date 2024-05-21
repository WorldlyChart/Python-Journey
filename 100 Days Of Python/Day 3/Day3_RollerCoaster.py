# Roller coaster ticket machine
print("welcome to the rollercoaster")
height = int(input("what is your heigh in cm?"))

if height > 120:
    print("you can ride!")
    age = int(input("how old are you"))
    if age >= 18:
        tickets = int(12)
        print("Adult tickets are $12")
    elif age > 12:
        tickets = int(7)
        print("Youth tickets are $7")
    else:
        tickets = int(5)
        print("Child tickets are $5")
    wants_pictures = input("Pictures are $3 Do you want pictures taken? Y or N")
    
    if wants_pictures == "Y" or "y":
        total = tickets + int(3)
        print(f"Your total is {total}")
    else:
        total = tickets
        print(f"Your total is {total}")
else:
    print("sorry bye!")    
