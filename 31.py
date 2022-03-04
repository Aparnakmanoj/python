from graphics import circle
r=int(input("enter the radius of the circle:"))
circle.cir(r)
from graphics import rectangle
length = int(input("enter the length of the rectangle"))
breadth = int(input("enter the breadth of the rectangle"))
rectangle.rectt(length,breadth)
from graphics.package import cuboid
l = int(input("enter the length of the cuboid:"))
w = int(input("enter the width of the cuboid:"))
h= int(input("enter the height of the cuboid:"))
b = int(input("enter the breadth of the cuboid:"))
cuboid.cubo(l,w,h,b)
from graphics.package import sphere
r=int(input("enter the radius of sphere"))
sphere.sphe(r)