import random

def generate_random_number(start, end):
    return random.randint(start, end)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(f"Random number between {start} and {end} is {generate_random_number(start, end)}.")
