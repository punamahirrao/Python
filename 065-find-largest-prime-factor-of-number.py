def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

num = int(input("Enter a number: "))
print(f"The largest prime factor of {num} is {largest_prime_factor(num)}.")
