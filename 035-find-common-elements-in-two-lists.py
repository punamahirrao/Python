def common_elements(list1, list2):
    return list(set(list1).intersection(list2))

list1 = list(map(int, input("Enter first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter second list of numbers separated by space: ").split()))

print(f"Common elements: {common_elements(list1, list2)}")
