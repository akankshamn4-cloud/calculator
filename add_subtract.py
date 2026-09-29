# Python program for arithmetic operations

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Addition
addition = a + b

# Subtraction
subtraction = a - b

# Multiplication
multiplication = a * b

# Division
if b != 0:
    division = a / b
else:
    division = "Cannot divide by zero"

print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)