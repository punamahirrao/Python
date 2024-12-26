def sum_of_odds(lst):
    return sum(x for x in lst if x % 2 != 0)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The sum of odd numbers is {sum_of_odds(numbers)}.")
