###  POLIMORPHISM (ÇOK BİÇİMLİLİK)  ###

# Polimorphism aynı arayüzü paylaşan farklı nesnelerin farklı davranış sergileyebilmesine denir

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


rectangle1 = Rectangle(3, 7)
square1 = Square(4)
triangle1 = Triangle(6, 3)

shapes = [rectangle1, square1, triangle1]

for shape in shapes:
    print(f"The area: {shape.area()}")

for shape in (Rectangle(2, 5), Rectangle(6, 8), Square(5), Triangle(3, 8)):
    print(f"The area: {shape.area()}")





