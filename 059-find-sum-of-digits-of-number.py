def sum_of_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter a number: "))
print(f"The sum of digits of {num} is {sum_of_digits(num)}.")
