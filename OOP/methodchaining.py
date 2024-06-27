#method chaining = calling multiple methods sequentially
#method chaining is a way to simplify your code by calling multiple methods sequentially on the same object.        

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
        
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brake")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self
        
car = Car()

##car.turn_on().drive()

##car.brake().turn_off()
car.turn_on()\
    .drive()\
        .brake()\
            .turn_off()    