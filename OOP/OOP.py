# Class definition
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing attributes and calling methods
car1.display_info()  # Output: Car: Toyota Corolla
car2.display_info()  # Output: Car: Honda Civic
