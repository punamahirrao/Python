import math

def lcm_of_two_numbers(a, b):
    return abs(a * b) // math.gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The LCM of {num1} and {num2} is {lcm_of_two_numbers(num1, num2)}.")
