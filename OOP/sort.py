
#sort() method = used with lists
#sorted() function = used with any iterable



atla = [
    ("Aang", "Air", 80),
    ("Katara", "Water", 90),
    ("Sokka", "None", 50),
    ("Toph", "Earth", 95),
    ("Zuko", "Fire", 85)
]

#students.sort(reverse=True) #build in function to sort the list. IT WILL ONLY WORK with lists!!
element =lambda elements:elements[0] #this will sort the list by the first element of the tuple
power = lambda powers:powers[2] #this will sort the list by the power of the characters
atla.sort(key=element)

#sorted_atla = sorted(atla) #sorted() function will return a new list with the sorted elements

for i in atla:
    print(i)
    
    