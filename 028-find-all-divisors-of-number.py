def find_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return divisors

num = int(input("Enter a number: "))
print(f"The divisors of {num} are {find_divisors(num)}.")
