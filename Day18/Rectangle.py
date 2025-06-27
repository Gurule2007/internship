# Rectangle Class
# Private Attributes: __width and __height.

# Properties:

# width and height with getters and setters (no negatives).

# Method:

# area() returns the area of the rectangle.
class Rectangle:
    def __init__(self):
        self.__width =0
        self.__height=0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value >= 0:
            self.__width = value
        else:
            raise ValueError("Invalid width" )  

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        if value >= 0:
            self.__width = value
        else:
            raise ValueError("Invalid width" )  
        
        def area(self):
         return self.width * self.height


rect = Rectangle()
rect.width = 5

print(rect.area())
rect.height = -10