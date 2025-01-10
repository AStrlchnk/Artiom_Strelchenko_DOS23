import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius}, color='{self.color}')"

circle1 = Circle(2, "red")
circle2 = Circle(4, "blue")
circle3 = Circle(8, "green")

circles = [circle1, circle2, circle3]
for circle in circles:
    print(circle)
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}\n")