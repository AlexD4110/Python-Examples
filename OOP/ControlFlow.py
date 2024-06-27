# If-else statement
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
i = 1
while i < 5:
    print(i)
    i += 1

# Try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred.")
finally:
    print("Finally block always executed.")
