def median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The median of the list is {median(numbers)}.")
