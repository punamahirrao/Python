def convert_to_integers(lst):
    return [int(item) for item in lst]

strings = input("Enter a list of numbers as strings separated by space: ").split()
integers = convert_to_integers(strings)
print(f"List of integers: {integers}")
