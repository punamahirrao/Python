def convert_to_strings(lst):
    return [str(item) for item in lst]

integers = list(map(int, input("Enter numbers separated by space: ").split()))
strings = convert_to_strings(integers)
print(f"List of strings: {strings}")
