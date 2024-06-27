def count_vowels(s: str) -> int: #define count_vowels function that takes a single string parameter as 
    vowel_set = {'a', 'e', 'i', 'o','u'} #initalize a vowel set
    count = 0
    for vowel in s.lower():
        if vowel in vowel_set:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 3
print(count_vowels("Python Programming"))  # Output: 4
print(count_vowels("This is a test string"))  # Output: 5
print(count_vowels("AEIOU"))  # Output: 5
print(count_vowels(""))  # Output: 0

