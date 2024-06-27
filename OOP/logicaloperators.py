# logicla operators (and,or, not) + used to check if two or more conditional statemtns 

temp = float(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("the temperature is bad today!")
    print("You should stay inside")
elif not(temp < 0 or temp >30):
    print("The temp is goo")
    print("Go outside")



