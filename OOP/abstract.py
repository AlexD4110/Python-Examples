from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        print("Stopping")

class Car(Vehicle):

    def go(self):
        print("You drive the car")
        
    def stop(self):
        print("Car is going to be Stopping")

class Motorcycle(Vehicle):

    def go(self):
        print("you ride the motorcyle")
        
    def stop(self):
        print("Motororcyle is Stopping")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()


#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()