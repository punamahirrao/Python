def find_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

lst = list(map(int, input("Enter numbers separated by space: ").split()))
value = int(input("Enter value to search for: "))
index = find_index(lst, value)
if index != -1:
    print(f"Value {value} found at index {index}.")
else:
    print(f"Value {value} not found.")
