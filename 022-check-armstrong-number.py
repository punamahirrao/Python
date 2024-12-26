def is_armstrong(num):
    digits = len(str(num))
    total = sum(int(digit) ** digits for digit in str(num))
    return total == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
