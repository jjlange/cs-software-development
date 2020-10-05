# Live Session - 5/10/2020 - 4CSE05
# Question 4c

meal = int(input("Enter the cost of the meal: "))
print("Level 1: Totally satisfied, 2 = Satisfied, 3 = Dissatisfied")

level = int(input("Enter your satisfaction level: "))

if level == 1:
    total = ((meal * 20) / 100)
    print("Totally, satisfied. Tip: £" + str(total))
elif level == 2:
    total = ((meal * 15) / 100)
    print("Satisfied. Tip: £" + str(total))
elif level == 3:
    total = ((meal * 10) / 100)
    print("Dissatisfied. Tip: £" + str(total))
else:
    print("Enter a valid satisfaction level!")