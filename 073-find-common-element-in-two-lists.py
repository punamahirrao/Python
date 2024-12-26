def common_elements(list1, list2):
    return list(set(list1).intersection(list2))

list1 = list(map(int, input("Enter first list separated by space: ").split()))
list2 = list(map(int, input("Enter second list separated by space: ").split()))
print(f"The common elements are: {common_elements(list1, list2)}")
