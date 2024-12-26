def max_difference(lst):
    return max(lst) - min(lst)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The maximum difference between two numbers is {max_difference(numbers)}.")
