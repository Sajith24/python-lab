class Rectangle:
    def __init__(self):
        self._length = int(input("Enter the length: "))
        self._breadth = int(input("Enter the breadth: "))
        self._area = self._length * self._breadth

    def greaterThan(self, other_rectangle):
        if self._area < other_rectangle._area:
            print("Area of rect 1 is greater.")
        else:
            print("Area of rect 2 is greater.")

print("Rectangle 1:")
r1 = Rectangle()
print("Rectangle 2:")
r2 = Rectangle()
print("Comparing rectangles:")
r2.greaterThan(r1)
