
def is_palindrome(s: str) -> bool:
    
    s = ''.join(char.lower() for char in s if char.isalnum())
# This code is saying s is equal removing the spaces of the string and converting it to be a string without character such as punction


    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("Was it a car or a cat I saw?"))  # Output: True
print(is_palindrome("No 'x' in Nixon"))  # Output: True
