#Problem: Check if a given string is a palindrome (reads the same backward and forward).

def is_palindrome(s):
    return s == s[::-1]


word = "rada"
print(is_palindrome(word))  # Output: True
