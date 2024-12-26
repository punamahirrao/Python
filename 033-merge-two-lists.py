def merge_lists(list1, list2):
    return list1 + list2

list1 = list(map(int, input("Enter first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter second list of numbers separated by space: ").split()))

merged_list = merge_lists(list1, list2)
print(f"Merged list: {merged_list}")
