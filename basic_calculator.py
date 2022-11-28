
# Asking the user about numbers and the operator they want to add.
# And also telling them what are the operator signs
print("Welcome to our basic calculator!\nto add: +\nto substract: -\nto multiply: *\nto divide: /")
while (True) :

    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        print("Sum of the numbers is ", num1+num2)
    elif operator == "-":
        print("Difference between the numbers is ", num1-num2)
    elif operator == "*":
        print("Product of the numbers is ", num1*num2)
    elif operator == "/":
        print("Division of num1 by num2 is ", num1/num2)
    else:
        print("Invalid Operator!")

    QUIT = input("Do you want to quit?")
    QUIT_ = QUIT.lower()
    if QUIT_ == "yes":
        break
    else:
        continue