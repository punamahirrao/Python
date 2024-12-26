from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The most frequent element is {most_frequent(lst)}.")
