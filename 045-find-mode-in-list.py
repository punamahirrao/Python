from collections import Counter

def mode(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The mode of the list is {mode(numbers)}.")
