import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())

sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print(f"'{sentence}' is a pangram.")
else:
    print(f"'{sentence}' is not a pangram.")
