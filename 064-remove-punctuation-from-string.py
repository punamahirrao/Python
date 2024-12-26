import string

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

text = input("Enter a string: ")
print(f"Text without punctuation: {remove_punctuation(text)}")
