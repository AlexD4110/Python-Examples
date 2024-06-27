class Person:
    def __init__(self, name, age):
        self.name = name  # setting the name attribute
        self.age = age    # setting the age attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

# Calling a method
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.


'''
1.	Class Definition:
	•	class Person: defines a new class called Person.
	2.	__init__ Method:
	•	def __init__(self, name, age): defines the __init__ method with self, name, and age as parameters.
	•	self.name = name and self.age = age initialize the object’s attributes.
	3.	Creating an Instance:
	•	person1 = Person("Alice", 30) creates a new instance of the Person class, automatically calling the __init__ method and passing the arguments "Alice" and 30.
	4.	Accessing Attributes and Methods:
	•	print(person1.name) and print(person1.age) access the attributes of person1.
	•	person1.greet() calls the greet method of person1.

Key Points

	•	self Parameter:
	•	The self parameter refers to the instance of the class and allows access to its attributes and methods. It must be the first parameter of any method in the class.
	•	Automatic Call:
	•	The __init__ method is called automatically when a new instance of the class is created.
	•	Initialization:
	•	It’s commonly used to initialize the object’s attributes with the values provided as arguments when the object is created.

The __init__ method is crucial for setting up the initial state of an object and ensuring that it has all the necessary attributes when it’s created.



'''