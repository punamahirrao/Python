def largest_element(lst):
    return max(lst)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The largest number in the list is {largest_element(numbers)}.")
