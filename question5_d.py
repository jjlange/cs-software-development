# Live Session - 5/10/2020 - 4CSE05
# Question 5d

mark = int(input("Enter a mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 70:
    print("Exceptional result!")
elif mark >= 40:
    print("Satisfactory result!")
else:
    print("You have failed.")
