# Problem: Find the missing number in an array of integers from 1 to n.

def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


nums = [1, 2, 4, 5]
n = 5
print(find_missing_number(nums, n))  # Output: 3
