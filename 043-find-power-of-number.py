def power(base, exp):
    return base ** exp

base = float(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
print(f"{base} raised to the power {exp} is {power(base, exp)}.")
