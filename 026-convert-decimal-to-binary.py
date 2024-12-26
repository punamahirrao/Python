def decimal_to_binary(n):
    return bin(n).replace("0b", "")

num = int(input("Enter a decimal number: "))
print(f"The binary representation of {num} is {decimal_to_binary(num)}.")
