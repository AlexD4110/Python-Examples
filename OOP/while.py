#while loop = a statment that will execute it's block of code,
# as long as its condtion remains ture

name = ""

while len(name) == 0:
    name = input("enter your name:")

print("Hello "+name)


name = None

while not name:
    name = input("Enter your name:")
print("Hello "+name)