class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breath)
rectangle1=rectangle(5,10)
rectangle2=rectangle(8,6)
area1=rectangle1.area()
area2=rectangle2.area()
print("area of rectangle 1:")
print("area of rectangle 2:")
if area1>area2:
    print("rect 1 has larger area")
elif area1<area2:
    print("rect 2  has a larer area")
else:
    print("same area")
