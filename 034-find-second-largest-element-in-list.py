def second_largest(lst):
    lst = list(set(lst))  # Remove duplicates
    lst.sort()
    return lst[-2] if len(lst) > 1 else None

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The second largest element is {second_largest(numbers)}")
