# Experiment No: 08
# Experiment Name:
# Write a program using Python to determine the Greatest Common Divisor of two positive integer numbers.
# Source Code:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
 a, b = b, a % b
print("GCD =", a)

# Output:
# Enter first number: 12
# Enter second number: 24
# GCD = 12
