

def hello(**kwargs):
    print("Hello", end =" ")
   # print("Hello " + kwargs['first'] + " "+ kwargs["last"])
    for key,value in kwargs.items():
        print(value, end=" ")
hello(title= "Mr." ,first = "Alex", middle = "Joseph", last = "Deane")

