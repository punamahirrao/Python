def is_all_digits(s):
    return s.isdigit()

string = input("Enter a string: ")
if is_all_digits(string):
    print(f"The string contains only digits.")
else:
    print(f"The string contains non-digit characters.")
