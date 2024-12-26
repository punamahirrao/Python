def sort_list(lst):
    return sorted(lst)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Sorted list: {sort_list(numbers)}")
