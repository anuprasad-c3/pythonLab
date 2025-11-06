import graphics.rectangle
from graphics import circle
from graphics.threeDgraphics import cuboid,sphere

l = float(input("Enter the length of rectangle :"))
b = float(input("Enter the breadth of rectangle :"))
print("\n---Rectangle---\n")
print("Area :",graphics.rectangle.area(l,b))
print("Perimeter :",graphics.rectangle.perimeter(l,b))

r = float(input("\nEnter the radius of the circle :"))
print("\n---circle---")
print("Area :",circle.area(r))
print("Perimeter :",circle.perimeter(r))

l = float(input("Enter the length of cuboid :"))
b = float(input("Enter the breadth of cuboid :"))
h = float(input("Enter the height of cuboid :"))
print("\n---Cuboid---\n")
print("Surface area :",cuboid.surface_area(l,b,h))
print("Volume :",cuboid.volume(l,b,h))

r = float(input("\nEnter the radius of sphere :"))
print("\n---Sphere---")
print("Surface area :",sphere.surface_area(r))
print("Volume :",sphere.volume(r))
