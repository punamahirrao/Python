import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
print(f"The length of the hypotenuse is {hypotenuse(side1, side2):.2f}.")
