
def longest_palindromic_substring(s):
    if not s:
        return ""

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    start, end = 0, 0
    
    for i in range(len(s)):
        # Odd length palindromes
        left1, right1 = expand_around_center(s, i, i)
        # Even length palindromes
        left2, right2 = expand_around_center(s, i, i + 1)
        
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    
    return s[start:end + 1]

# Example usage
s1 = "babad"
result1 = longest_palindromic_substring(s1)
print(result1)  # Output: "bab" or "aba"

s2 = "cbbd"
result2 = longest_palindromic_substring(s2)
print(result2)  # Output: "bb"
