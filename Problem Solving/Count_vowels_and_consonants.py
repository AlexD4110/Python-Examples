
from typing import Tuple

def Count_vowels_and_consonants(s:str) -> Tuple[int, int]:
    vowel_set = {'a', 'e', 'i', 'o', 'u'}#init vowel set
    vowels_count = 0    #init vowel_count
    consonants_count =0    #init consonant_count
    
    s = s.lower()

    for char in s:
        if char.isalpha():
            if char in vowel_set:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count










# Example usage:
result = Count_vowels_and_consonants("Hello, World!")
print(f"Vowels: {result[0]}, Consonants: {result[1]}")  # Output: Vowels: 3, Consonants: 7

result = Count_vowels_and_consonants("This is a test sentence.")
print(f"Vowels: {result[0]}, Consonants: {result[1]}")  # Output: Vowels: 7, Consonants: 10

result = Count_vowels_and_consonants("Python is awesome!")
print(f"Vowels: {result[0]}, Consonants: {result[1]}")  # Output: Vowels: 5, Consonants: 9
