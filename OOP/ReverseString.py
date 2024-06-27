
def reverse_string(s: str) -> str: # takes string as input
    reversed_s = "" #initialize
    for char in s.strip().lower(): #for each character in s
        reversed_s = char + reversed_s #return char +
    return reversed_s

print(reverse_string("Dinosaur is REALLY BIG"))

