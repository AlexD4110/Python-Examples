'''# Define a function to square a number
def square(x):
    return x ** 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each element in the list
squared_numbers = list(map(square, numbers))

# Print the squared numbers
print(squared_numbers)'''
import math

# Create a variable named restaurant with 40 tuples
restaurant = [
    ("Pizza", 20.00),
    ("Burger", 15.00),
    ("Pasta", 18.50),
    ("Salad", 12.00),
    ("Steak", 25.00),
    ("Chicken", 17.00),
    ("Sushi", 22.50),
    ("Fries", 8.00),
    ("Ice Cream", 6.00),
    ("Coffee", 4.50),
    ("Tea", 3.00),
    ("Soda", 2.50),
    ("Water", 1.00),
    ("Juice", 3.50),
    ("Milk", 2.00),
    ("Beer", 5.00),
    ("Wine", 7.00),
    ("Whiskey", 10.00),
    ("Vodka", 8.50),
    ("Rum", 9.00),
    ("Gin", 7.50),
    ("Tequila", 9.50),
    ("Brandy", 12.50),
    ("Cognac", 15.50),
    ("Champagne", 20.50),
    ("Cocktail", 18.00),
    ("Mocktail", 10.50),
    ("Lemonade", 5.50),
    ("Margarita", 7.50),
    ("Martini", 9.50),
    ("Mojito", 8.00),
    ("Cosmopolitan", 10.00),
    ("Bloody Mary", 6.50),
    ("Gimlet", 5.00),
    ("Screwdriver", 4.00),
    ("Mai Tai", 7.00),
    ("Pina Colada", 8.50),
    ("Long Island Iced Tea", 10.50),
    ("Blue Lagoon", 9.00),
]

to_euros = lambda data: (data[0], data[1]*0.85)
to_dollars = lambda data: (data[0], data[1]/0.85)
restaurant_dollars = list(map(to_dollars, restaurant))
for i in restaurant_dollars:
    print(i)
