def find_first_occurrence(string, substring):
    return string.find(substring)

string = input("Enter a string: ")
substring = input("Enter substring to search for: ")
index = find_first_occurrence(string, substring)
if index != -1:
    print(f"The first occurrence of '{substring}' is at index {index}.")
else:
    print(f"'{substring}' not found in the string.")
