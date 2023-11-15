import math
def area(r):
    return math.pi*r*r
def perimeter(r):
    return 2*math.pi*r
r=int(input("enter the radius:"))
print("area of circle:",area(r))
print("perimeter of a circle:",perimeter(r))
