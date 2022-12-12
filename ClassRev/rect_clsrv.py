#Cody Brown, Fnal Exam Review, Class cont. Rectangle Example!

 # CLASS RECTANGLE EXAMPLE
# We decide we want to create a class that represents a rectangle. We have to think,
# what attributes should we use to make it possible to describe the location and size
# of a rectangle?
    # Some things we could do:
        # specify one corner or the center of the rectangle with width and height
        # specify two opposing corner

#NEEDED FROM PREVIOUS EXAMPLE:
class Point: #this header indicates the name of the class
    """Represents a point in 2-D space""" #this is called the docstring, which explains
                                          #what the class is for

#DEFINING THE CLASS
class Rectangle:
    '''Represents a rectangel

    attributes: width, height, corner'''
 # recall, we have our header with the name of the class, and then the docstring in then
 # body that explains things about the class

# Making the width and height
box = Rectangle()
box.width = 100.0
box.height = 200
# Making the corner
box.corner = Point()
# an object that is an attribute of another object is embedded
box.corner.x = 0.0
box.corner.y = 0.0

print(type(Rectangle))
    # <class 'type'>
print(type(Point))
    # <class 'type'>
print(type(box.corner))
    # <class '__main__.Point'>
print(type(box.corner.x))
    # <class 'float'>

 # OBJECTS AS RETuRN VALUES
# functions can return objects:
def find_center(rect): #this takes a Rectangles as an argument
    p = Point() #makes a constructor called p for Point class
    p.x = rect.corner.x + rect.width/2 #assigns p.x as the following
    p.y = rect.corner.y + rect.height/2 #assigns p.y as the following
    return p # this will then return a Point that contains the coordinates
             # of the center of the rectangle

def print_point(p):
    print('(%g, %g)'%(p.x,p.y))

center = find_center(box) #finding the center of class Rectangle, constructor box
print_point(center) #printing the point of the above result
    # this prints: (50, 100)

 # OBJECT MUTABILITY
# we can change the state of object by making an assignment to one of its attributes:
print('before changing', box.width)
print('before changing', box.height)
    # before changing 100.0
    # before changing 200
#---------
box.width = box.width + 50
box.height = box.height + 100
#---------
print(box.width)
print(box.height)
    # we get two new values for width and height:
    # 150.0
    # 300.0

# we can also wirte a function that will modify objects:
def grow_rectangle(rect, gwidth, gheight): #rect is an alias for box, gwidth and gheight is
    rect.width += gwidth                   #how much we want to grow the height/width by
    rect.height += gheight

grow_rectangle(box, 10, 10)
print(box.width)
print(box.height)
    # prints:
    # 160.0
    # 310

 # COPYING
# The aliasing you notie in find_center and grow_rectangle, rect, is called an alias
# these can get confusing, so another option is to copy!
# copying is a module:
import copy

p1 = Point()
p1.x = 3.0
p1.y = 4.0

p2 = copy.copy(p1)
print(p1 == p2)
    # prints: False

# This is referred to as shallow copying because it only copies the object and
# any references it contains, BUT NOT EMBEDDED OBJECTS

# Deep coping allows for the object and object it is referring to:
box1 = copy.deepcopy(box)
print(box1.width == box.width)
# returns True!
print(box1.corner.x == box.corner.x)
# this also returns True!
    # why? Attributes can be copied, but use deep copy. Shadow copy
    # will work on not class things
