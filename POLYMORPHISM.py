class Shape:
    def printVal(self):
        print("Shape")

class Circle:
    def printVal(self):
        print("Circle")

class Rectangle:
    def printVal(self):
        print("Rectangle")

class Square:
    def printVal(self):
        print("Square")

class A:
    def draw(self, a:Shape):
        a.printVal()

obj = A()
obj.draw(Shape())
obj.draw(Circle())
obj.draw(Rectangle())
obj.draw(Square())