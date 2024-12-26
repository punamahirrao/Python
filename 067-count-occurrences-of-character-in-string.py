def count_char(s, char):
    return s.count(char)

string = input("Enter a string: ")
char = input("Enter a character to count: ")
print(f"The character '{char}' appears {count_char(string, char)} times.")
