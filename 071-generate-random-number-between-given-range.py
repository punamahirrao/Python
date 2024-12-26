import random

def random_number(start, end):
    return random.randint(start, end)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"A random number between {start} and {end} is {random_number(start, end)}.")
