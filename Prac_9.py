print("Archana Vyas 20Ce157")
class Point(object):
    """Represents a point in 2d space"""


class Rectangle(object):
    """Represents a rectangle in 2d space"""

rectangle = Rectangle()

bottom_left = Point()
bottom_left.x = float(input("Enter the Bottom Left value of x cordinate: "))
bottom_left.y = float(input("Enter the Bottom Left value of y cordinate: "))

top_right = Point()
top_right.x = float(input("Enter the Top Right value of x cordinate: "))
top_right.y = float(input("Enter the Top Right value of y cordinate: "))

rectangle.corner1 = bottom_left
rectangle.corner2 = top_right

dx = float(input("\nEnter value of dx: "))
dy = float(input("Enter value of dy: "))


def move_rectangle(rectangle, dx, dy):
    """Takes a rectangle and moves it to the values of dx and dy."""
    print ("\nThe rectangle started with bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and top right corner at (%g,%g)."
           % (rectangle.corner2.x, rectangle.corner2.y)),
    print("dx is %g and dy is %g" % (dx, dy))
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print ("\nIt ended with a bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and a top right corner at (%g,%g)"
           % (rectangle.corner2.x, rectangle.corner2.y))

move_rectangle(rectangle, dx, dy)