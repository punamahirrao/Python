def reverse_number(n):
    return int(str(n)[::-1])

num = int(input("Enter a number: "))
print(f"The reverse of {num} is {reverse_number(num)}.")
