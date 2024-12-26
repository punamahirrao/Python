def binary_to_decimal(b):
    return int(b, 2)

binary = input("Enter a binary number: ")
print(f"The decimal representation of {binary} is {binary_to_decimal(binary)}.")
