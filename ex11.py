num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
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