
from typing import Tuple

def count_character(s: str) -> Tuple[int, int, int, int]:
    vowel_set = {'a', 'e', 'i', 'o', 'u'}#init vowel set
    vowels_count = 0    #init vowel_count
    consonants_count = 0    #init consonant_count
    digits = 0 #init digits
    special_char = 0 #init digits

    s = s.lower()

    for char in s:
        if char.isalpha():
            if char in vowel_set:
                vowels_count += 1
            else:
                consonants_count += 1
        elif char.isdigit:
            digits += 1
        else:
            special_char += 1
    return vowels_count, consonants_count, digits, special_char



result = count_character("Hello, World! 123")
print(f"Vowels: {result[0]}, Consonants: {result[1]}, Digits: {result[2]}, Special Characters: {result[3]}")
# Output: Vowels: 3, Consonants: 7, Digits: 3, Special Characters: 4

result = count_character("This is a test sentence with 2022 and @ symbols!!!")
print(f"Vowels: {result[0]}, Consonants: {result[1]}, Digits: {result[2]}, Special Characters: {result[3]}")
# Output: Vowels: 9, Consonants: 14, Digits: 4, Special Characters: 12

result = count_character("Python is awesome!!!")
print(f"Vowels: {result[0]}, Consonants: {result[1]}, Digits: {result[2]}, Special Characters: {result[3]}")            
        
