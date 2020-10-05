# Live Session - 5/10/2020 - 4CSE05
# Question 4a

print("Usage: 0 to convert from Fahrenheit to Celsius")
print("Usage: 1 to convert from Celsius to Fahrenheit")

unit = int(input("Enter unit: "))

if unit == 0:
    f = int(input("Enter in Fahrenheit: "))
    c = (f - 32) / 1.8
    print(f"{f}C = {c}F")
elif unit == 1:
    c = int(input("Enter in Celsius: "))
    f = (c * 1.8) + 32
    print(f"{c}C = {f}F")
else:
    print("Please enter a valid unit!")