# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function call
result = greet("Alice")
print(result)  # Output: Hello, Alice!

# Function with default arguments
def greet_default(name="Anonymous"):
    return f"Hello, {name}!"

result = greet_default()
print(result)  # Output: Hello, Anonymous!

# Function with keyword arguments
def greet_with_message(name, message="Good day"):
    return f"{message}, {name}!"

result = greet_with_message("Bob", message="Hello")
print(result)  # Output: Hello, Bob!
