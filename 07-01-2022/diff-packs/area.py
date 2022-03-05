from Graphics import rectangle,circle
from Graphics.ThreeDGraphics import cuboid,sphere
l=int(input("Enter the length of the Rectangle:"))
b=int(input("Enter the breadth of the Rectangle:"))
rectangle.rectarea(l,b)
rectangle.perimetre(l,b)
r=int(input("Enter the radius of the Circle:"))
circle.cirarea(r)
l=int(input("Enter the length of Cuboid:"))
b=int(input("Enter the breadth of Cuboid:"))
h=int(input("Enter the height of Cuboid:"))
cuboid.cubarea(l,b,h)
r=int(input("Enter the radius of Sphere:"))
sphere.sparea(r)
sphere.spperimetre(r)

