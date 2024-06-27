
def is_palindrome(s):
    normalstring = "".join(char.lower() for char in s if char.isalnum())
    left = 0
    right = len(normalstring) -1
    while left < right:
        if normalstring[left] != normalstring[right]:
               return False
        left += 1
        right -= 1
               
    return True



s1 = "PULL UP IF I PULL UP"
print(is_palindrome(s1))




#defining a function to check if word is a palindrome
 #variable need method to joing the words together
         #make the letters all lower or all upper
         #needs to check for alphabet characters only
         #need to pass this as a variable
 #create left variable and right variable
         #left variable should start from beginning (0)
         #right should start from the end len(normalized_variable)
    #need to check if the left if less then right side
         #When the left is bigger if means that the there won't be a middle that can lead to palindrom