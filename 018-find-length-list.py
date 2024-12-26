def list_length(lst):
    return len(lst)

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The length of the list is {list_length(lst)}.")
