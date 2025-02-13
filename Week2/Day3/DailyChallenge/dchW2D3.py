import math
import turtle

# The goal is to create a class that represents a simple circle.

class Circle:
    list_circles = []

    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = int(radius)
            self.diameter = self.radius * 2
        elif diameter is not None:
            self.diameter = int(diameter)
            self.radius = self.diameter // 2
        else:
            raise ValueError("Either radius or diameter must be provided.")
        Circle.list_circles.append(self)

# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
    def area(self):
            return math.pi * self.radius ** 2
# Print the attributes of the circle - use a dunder method
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"
    def __repr__(self):
        return f"Circle({self.radius})"
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius
# Be able to put them in a list and sort them
    @classmethod
    def sorted_list(cls):
        return sorted(cls.list_circles, key=lambda c: c.radius)
         
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles
# Draw all circles in one window
    @classmethod
    def draw_all(cls):
        screen = turtle.Screen()
        t = turtle.Turtle()

        for circle in cls.list_circles:
            t.circle(circle.radius)


        t.hideturtle()
        screen.mainloop() 

        

# Create circle instances
circ1 = Circle(radius=50)
circ2 = Circle(diameter=100)

# Print values
print(circ1.area())  
print(circ2.radius)  
print(circ1 + circ2)  
print(circ1 > circ2)  
print(circ1 == circ2)  

Circle.draw_all()