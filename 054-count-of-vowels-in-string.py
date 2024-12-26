def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

string = input("Enter a string: ")
print(f"The number of vowels in the string is {count_vowels(string)}.")
