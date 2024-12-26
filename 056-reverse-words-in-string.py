def reverse_words(s):
    words = s.split()
    return " ".join(reversed(words))

string = input("Enter a sentence: ")
print(f"Reversed words: {reverse_words(string)}")
