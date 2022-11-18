# CS 1400, HOMEWORK 10, file 2
# DUE: Thursday, 03/29/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515




# Problem 8_18






####==================####
#### NOTES FOR GRADER ####
####==================####
'''
(A.)  How I interpreted "contains":
   -- for the point, I said that it is contained within the circle if it lies exactly on the perimeter or
      anywhere within the circle itself.
   -- for the circle, I said that it is contained within the other circle if it lies entirely within the
      outer circle, or if it lies entirely within and also has exactly one point of intersection with the
      outer circle.

(B.) How I understood "overlaps":
    CASES constituting overlap:
    1. The two circles are the same (in terms of center coords and radius) -- counts as overlap
    2. One circle is within the other (check both ways) -- counts as overlap
    3. The two circles touch at only one point (where the distance between their center pts is equal to
       the sum of their radii) -- counts as overlap
    4. The two circles touch at two points (the distance between their center pts is less than the sum of
       their radii) -- counts as overlap

'''








'''
PROGRAM TITLE: "Geometry: The Circle2D class"

Define the Circle2D class that contains:
-- two private float data fields named x and y that specify the center of the circle with get/set methods.
-- A private data field radius with get/set methods.
-- A constructor that creates a cricle with the specified x, y, and raidus. The default values are all 0.
-- A method getArea() that returns the area of the circle.
-- A method getPerimeter() that returns the perimeter of the circle.
-- A method containsPoint(x,y) that returns True if the specified point (x,y) is inside this circle.
-- A method contains(circle2D) that returns True if the specified circle is inside this circle.
-- A method overlaps(circle2D) that returns True if the specified circle overlaps with this circle.
-- Implement the __contains__(another) method that returns True if this circle is contained in another circle.
-- Implement the __cmp__, __lt__, __le__, __eq__, __ne__, __gt__, __ge__ methods that compare two circles
   based on their radii.




Draw the UML diagram for the class, and then implement the class. Write a test program that:
-- prompts the user to enter two circles with an x-coord and a y-coord and the radius
-- creates two Circle2D objects c1 and c2
-- displays their areas and perimeters
-- displays the result of c1.containsPoint(c2.getX(), c2.getY()), c1.contains(c2), and c1.overlaps(c2).


Here is a sample run:

    Enter x1, y1, radius1: 5, 5.5, 10
    Enter x2, y2, radius2: 9, 1.3, 10
    Area for c1 is 314.1519......
    Perimeter for c1 is 62.8318......
    Area for c2 is 314.1519......
    Perimeter for c2 is 62.8318......
    c1 contains the center of c2? True
    c1 contains c2? False
    c1 overlaps c2? True

'''






'''
HERE IS MY UML DIAGRAM

--------------------------------------------------------------------------------------------------------
        Circle2D                                                                    <-- CLASS NAME             
--------------------------------------------------------------------------------------------------------
x: float                                                                            <-- DATA FIELDS           
y: float                                                                              <-/     
radius: float                                                                        <-/
--------------------------------------------------------------------------------------------------------
Circle2D(x:float, y:float, radius:float)                                            <-- CONSTRUCTOR     
getX(): float                                                                       <-- METHODS
getY(): float                                                                         <-/                
getRadius(): float                                                                   <-/
setX(x:float): none                                                                 <-/            
setY(y:float): none                                                                <-/
setRadius(radius:float): none                                                     <-/
getArea(): float                                                                 <-/
getPerimeter(): float                                                           <-/
containsPoint(x:float, y:float): boolean                                       <-/
contains(cObject:Circle2D): boolean                                           <-/
overlaps(cObject:Circle2D): boolean                                          <-/       

NOTE: I didn't include any of the __lt__, __le__, etc. fctns in this diagram because Andy
      said that we didn't need to. Also, he said we didn't need to do the __cmp__ fctn or         
      the __contains__ fctn either.                     
--------------------------------------------------------------------------------------------------------
'''




#       Because we'll be calculating the area and circumference of circle objects, we'll need access to the
# value of pi. This value can be accessed using the 'math' library, so let's import it.
#       Also, following convention from previous instruction, since pi is a constant, let's make it an ALL-CAPS
# named constant.
import math
PI = math.pi



# Define the Circle2D class.
class Circle2D:

    # Constructor function, sets default values of 0 for x, y, and radius data fields.
    def __init__(self, x = 0, y = 0, radius = 0):
        self.__x = x
        self.__y = y
        self.__radius = radius
        
        
    # Accessor (getter) functions for the data fields x, y, and radius.
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getRadius(self):
        return self.__radius
    
    
    # Mutator (setter) functions for the data fields x, y, and radius.
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setRadius(self, radius):
        self.__radius = radius
        
        
    # This function calculates and returnss the area of a Circle2D object.
    def getArea(self):
        return (PI*self.__radius*self.__radius)
    
    
    # This function calculates and returns the perimeter (more commonly referred to as circumference) of the
    # circle object.
    def getPerimeter(self):
        return (2*PI*self.__radius)


    # Returns True if the specified point (x,y) is inside this circle, False otherwise.
    # See NOTE at top of file for my understanding of a point being "contained" within a circle.
    def containsPoint(self, x, y):
        distFromPtToCenter = math.sqrt((self.__x - x)**2 + (self.__y - y)**2)
        if(distFromPtToCenter <= self.__radius):
            return True
        else:
            return False

        
    # Returns True if the specified circle is inside this circle, False otherwise.
    # See NOTE at top of file for my understanding of a circle being "contained" within another circle.
    def contains(self, innerCircObj):
        distBtwnCenters = math.sqrt((self.__x - innerCircObj.getX()) ** 2 + (self.__y - innerCircObj.getY()) ** 2)
        maxDistForContainment = math.fabs(self.__radius - innerCircObj.getRadius())
        # A circle with a larger radius than the other cannot be contained within the other.
        if(self.__radius < innerCircObj.getRadius()):
            return False
        elif (distBtwnCenters <= maxDistForContainment):
            return True
        else:
            return False





# Returns True if the specified circle overlaps with this circle, returns False otherwise
# CASES constituting overlap:
    # 1. The two circles are the same (in terms of center coords and radius) -- counts as overlap
    # 2. One circle is within the other (check both ways) -- counts as overlap
    # 3. The two circles touch at only one point (where the distance between their center pts is equal to
    #    the sum of their radii) -- counts as overlap
    # 4. The two circles touch at two points (the distance between their center pts is less than the sum of
    #    their radii) -- counts as overlap
    def overlaps(self, otherCircObj):
        distBtwnCenters = (math.sqrt((self.__x - otherCircObj.getX()) ** 2 + (self.__y - otherCircObj.getY()) ** 2))
        # Check case 1.
        if((self.__x == otherCircObj.getX()) and (self.__y == otherCircObj.getY()) and (self.__radius == otherCircObj.getRadius())):
            return True
        # Check case 2.
        elif(self.contains(otherCircObj) or otherCircObj.contains(self)):
            return True
        # Check cases 3 and 4.
        elif (distBtwnCenters <= (self.__radius + otherCircObj.getRadius())):
            return True
        else:
            return False


# Implement the __cmp__, __lt__, __le__, __eq__, __ne__, __gt__, __ge__ methods that compare two circles
# based on their radii.
    def __lt__(self, otherCircObj):
        return (self.__radius < otherCircObj.getRadius())

    def __le__(self, otherCircObj):
        return (self.__radius <= otherCircObj.getRadius())

    def __eq__(self, otherCircObj):
        return (self.__radius == otherCircObj.getRadius())

    def __ne__(self, otherCircObj):
        return (self.__radius != otherCircObj.getRadius())

    def __gt__(self, otherCircObj):
        return (self.__radius > otherCircObj.getRadius())

    def __ge__(self, otherCircObj):
        return (self.__radius >= otherCircObj.getRadius())

    def __contains__(self, otherCircObj):
        return (self.contains(otherCircObj))

    def __cmp__(self, otherCircObj):
        return (id(self) == id(otherCircObj))





'''
Write a test program that:
-- prompts the user to enter two circles with an x-coord and a y-coord and the radius
-- creates two Circle2D objects c1 and c2
-- displays their areas and perimeters
-- displays the result of c1.containsPoint(c2.getX(), c2.getY()), c1.contains(c2), and c1.overlaps(c2).
'''
def main():
    # Prompt the user to create two circles by entering the x-coord, y-coord, and radius as a tuple.
    x1,y1,radius1 = eval(input("Enter the circle #1 info in the following way: x,y,radius:"))
    x2,y2,radius2 = eval(input("Enter the circle #2 info in the following way: x,y,radius:"))

    # Create two Circle2D objects, c1 and c2.
    c1 = Circle2D(x1,y1,radius1)
    c2 = Circle2D(x2,y2,radius2)

    # Display the areas and perimeters of c1 and c2.
    print("The area of c1 is:", c1.getArea())
    print("The area of c2 is:", c2.getArea())
    print("The perimeter of c1 is:", c1.getPerimeter())
    print("The perimeter of c2 is:", c2.getPerimeter())

    # Display the results of c1.containsPoint(c2.getX(), c2.getY()), c1.contains(c2), and c1.overlaps(c2).
    print("Does c1 contain the center pt of c2?", c1.containsPoint(c2.getX(), c2.getY()))
    print("Does c1 contain c2?", c1.contains(c2))
    print("Does c1 overlap c2?", c1.overlaps(c2))

    # The directions don't call for this, but I'm going to implement all the __(  )__ functions we were
    # supposed to write so that you can see that they work:
    print("c1 < c2:", c1 < c2)
    print("c1 <= c2:", c1 <= c2)
    print("c1 == c2:", c1 == c2)
    print("c1 != c2:", c1 != c2)
    print("c1 > c2:", c1 > c2)
    print("c1 >= c2:", c1 >= c2)
    print("c1 in c2:", c1 in c2)
    print("c1.__cmp__(c2):", c1.__cmp__(c2))



# Call the main function
main()