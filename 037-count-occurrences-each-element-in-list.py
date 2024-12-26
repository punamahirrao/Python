from collections import Counter

def count_occurrences(lst):
    return dict(Counter(lst))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Occurrences of each element: {count_occurrences(numbers)}")
