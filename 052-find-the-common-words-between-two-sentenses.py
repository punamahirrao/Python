def common_words(sentence1, sentence2):
    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())
    return words1.intersection(words2)

sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")
print(f"Common words: {common_words(sentence1, sentence2)}")
