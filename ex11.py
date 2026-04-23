def calculator():
    """
    Simple calculator Exercise
    """
num1 = input("Enter the first number: ")
if not num1.replace('.', '', 1).isdigit():
    print("Error: Invalid input. Please enter a valid number.")
    exit(1)
num2 = input("Enter the second number: ")
if not num2.replace('.', '', 1).isdigit():
    print("Error: Invalid input. Please enter a valid number.")
    exit(1)
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    if float(num2) == 0:
        print("Error: Division by zero")
        exit(1)
    result = float(num1) / float(num2)
else:
    print("Error: Invalid operation")
    exit(1)

print("The result is: ", result)

__name__ == "__main__" and calculator() 