#if statment = a blocl of code that will execute if its's condition is true

age = int(input("How old are you?:" ))

if age == 100:
    print("You are ancient")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 18:
    print("You are an adult")
else:
    print("You are a baby")


