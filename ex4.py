
user = input("Enter the radius of the circle: ")
try:
    radius = float(user)
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is: {area}")
except ValueError:
    print("Invalid input. Please enter a number for the radius.")
