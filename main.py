def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    print("\n \n------------------------\n" \
        "Please select operation.\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "------------------------\n")
        
    selection = int(input("Select an operation from the following: 1/2/3/4\n	"))
    Number1 = int(input("Enter first number: "))
    Number2 = int(input("Enter second number: "))

    if selection == 1:
        print(Number1, " + ", Number2, " = ", add(Number1, Number2))
    elif selection == 2:
        print(Number1, " - ", Number2, " = ", subtract(Number1, Number2))
    elif selection == 3:
        print(Number1, " × ", Number2, " = ", multiply(Number1, Number2))
    elif selection == 4:
        print(Number1, " ÷ ", Number2, " = ", divide(Number1, Number2))
    continuing = str(input("Would you like another operation? yes/no\n	"))
    if continuing == "yes":
        continue
    else:
        exit()