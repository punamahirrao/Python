def sum_of_evens(lst):
    return sum(x for x in lst if x % 2 == 0)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The sum of even numbers is {sum_of_evens(numbers)}.")
