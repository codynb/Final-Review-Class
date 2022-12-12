#Cody Brown, Fnal Exam Review, Class!

 # QUESTION:
# How many different datatypes have we learned?
    # strings
    # objects
    # integers
    # floats
    # dictionary
    # lists

# Now, we are going to define a new type!

 # DEFINING A CLASS
# a programmer-defined type is called a class
# creating a class:
class Point: #this header indicates the name of the class
    """Represents a point in 2-D space""" #this is called the docstring, which explains
                                          #what the class is for
print(type(Point))
    # this prints <class 'type'>, we created a class object
    # this class object is like a factory to create objects
# To creat a point, we need to call Point like a function:
myPoint = Point()
# here, myPoint is called a constructor, which is a function with the same
# name as the class we created
print(type(myPoint))
# this prints: <class '__main__.Point'>, myPoint is an instance or object of
# the class Point, so it told us which class it belonged to

 # ASSIGING ATTRIBUTES IN A CLASS
# We use the dot notation as seen with all other modules
# we want to make a point value at x:
myPoint.x = 0
# we want to make another point value at y:
myPoint.y = 2

print(myPoint.x)
print(myPoint.y)
    # this prints:
    # 0
    # 2

# We can use this dot notation as a part of any expression:
print("(%d, %d)" %(myPoint.x, myPoint.y))
    # this prints: (0, 2)

# We can also use this dot notation inside a function:
import math
# we creat a funciton that will tell us the distance from the origin that our points are
def distance_from_origin(p):
    distance = math.sqrt(p.x**2 + p.y**2)
    print(distance)

distance_from_origin(myPoint)
    # this prints: 2.0

 
