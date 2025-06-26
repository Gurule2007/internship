class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        a= self.length * self.width
        print("The Area:-",a)

    def perimeter(self):
        b=2 * (self.length + self.width)
        print("The Perimeter:-",b)

rect = Rectangle(5,2)
rect.perimeter ()
rect.area()

