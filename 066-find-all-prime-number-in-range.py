def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    return [i for i in range(start, end+1) if is_prime(i)]

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers in the range are: {prime_numbers_in_range(start, end)}")
