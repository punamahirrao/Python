def flatten(lst):
    return [item for sublist in lst for item in sublist]

nested_list = [[1, 2, 3], [4, 5], [6]]
print(f"Flattened list: {flatten(nested_list)}")
