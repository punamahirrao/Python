def sum_of_squares(lst):
    return sum(x**2 for x in lst)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The sum of squares of the numbers is {sum_of_squares(numbers)}.")
