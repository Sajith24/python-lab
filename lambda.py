area_s=lambda a : a*a
area_rect=lambda l,b : l*b
area_triangle=lambda b1,h :0.5*b1*h
a=int(input("Enter the side of the square "))
print("Area of square ",area_s(a))
l=int(input("Enter the length of rectangle "))
b=int(input("Enter the breadth of rectangle "))
print("Area of rectangle ",area_rect(l,b))
b1=int(input("Enter the base of triangle "))
h=int(input("Enter the base of triangle "))
print("Area of triangle ",area_triangle(b1,h))
