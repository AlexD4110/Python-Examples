# super() = Function is used to call the parent class method from the child class method.
# returns a temporary object of a parent class when used


class Rectangle:
    
     def __init__(self, side_length, side_width):
        self.side_width = side_width
        self.side_length = side_length


class Square(Rectangle):
    def __init__(self, side_length, side_width):
        super().__init__(side_length, side_width)
        
    def area(self):
        return self.side_length * self.side_width  
        
class Cube(Square):
    def __init__(self, side_length, side_width, side_height):
        super().__init__(side_length, side_width)   
        self.side_height = side_height
    
    def volume(self):
        return self.side_length * self.side_width * self.side_height  
    
cube = Cube(1, 3, 9)
area = Square(3, 9)
print()
print(cube.volume())  
print(area.area())