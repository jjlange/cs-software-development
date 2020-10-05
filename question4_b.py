# Live Session - 5/10/2020 - 4CSE05
# Question 4b

x = int(input("First number: "))
op = input("Enter an operator: ")
y = int(input("Second number: "))

if op == "+":
    z = x + y
    print(z)
elif op == "-":
    z = x - y
    print(z)
elif op == "/":
    try:
        z = x / y
        print(z)
    except ZeroDivisionError:
        print("Error!")   
elif op == "*":
    z = x * y
    print(z)
else:
    print("Enter a valid operator.")    
