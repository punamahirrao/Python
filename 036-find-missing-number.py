def find_missing_number(lst, n):
    total_sum = (n * (n + 1)) // 2
    return total_sum - sum(lst)

numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
n = int(input("Enter the total number of elements including the missing one: "))
print(f"The missing number is {find_missing_number(numbers, n)}")
