#Problem: Find the first character in a string that doesn’t repeat.

from collections import Counter

def first_non_repeating_char(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

# Test
s = "swiss"
print(first_non_repeating_char(s))  # Output: "w"
