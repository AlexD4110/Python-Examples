

#lamda parameters:expression
#using one line

#def double(x):
 #   return x*2

#print(double(5)) 



double = lambda x: x*2
multiply = lambda x,y,z: x*y*z 
add = lambda x,y: x+y  
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age>=18 else False 
Age = int(input("Enter your age: "))
print(age_check(Age))
print(full_name("Jimmy", "Fallon"))

     
'''print(add(3,3))
print(multiply(3,9,2))
print(double(9))'''



