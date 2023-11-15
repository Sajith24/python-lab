import graphics.circle
import graphics.rectangle
import graphics.graphics3d.cuboid
import graphics.graphics3d.sphere
r=int(input("radius of circle:"))
r1=int(input("radius of sphere:"))
len=int(input("length of rectangle:"))
breadth=int(input("breadth of rectangle:"))
len=int(input("length of cuboid:"))
height=int(input("height of cuboid:"))
width=int(input("width of cuboid:"))

print("Area of circle:",graphics.circle.area(r))
print("Permeter of circle :",graphics.circle.perimeter(r))

print("Area of rectangle:",graphics.rectangle.area(len,breadth))
print("Permeter of rectangle :",graphics.rectangle.perimeter(len,breadth))

print("Area of a  cuboid  : ",graphics.graphics3d.cuboid.area(len,width,height))
print("Permeter of a cuboid : ",graphics.graphics3d.cuboid.perimeter(len,width,height))

print("Area of a sphere : ",graphics.graphics3d.sphere.area(r1))
print("Permeter of a sphere ",graphics.graphics3d.sphere.perimeter(r1))
