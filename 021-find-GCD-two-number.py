import math

def gcd_of_two_numbers(a, b):
    return math.gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The GCD of {num1} and {num2} is {gcd_of_two_numbers(num1, num2)}.")
