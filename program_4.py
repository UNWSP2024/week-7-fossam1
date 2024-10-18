#Samuel Foss
#Program 4 Coordinates
#10/15

# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math

def distance(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def collectcoord():
            coords = input("Input three number coordinates separated by commas: ")
            x, y, z = map(float, coords.split(','))
            return (x, y, z)

def main():
    print("Enter 3 coordinates of the first point:")
    c1 = collectcoord()
    print("Enter 3 coordinates of the second point:")
    c2 = collectcoord()

    dist = distance(c1, c2)
    print(f"The distance between point {c1} and {c2} is: {dist:.2f}")

if __name__ == "__main__":
    main()

#output
#Enter 3 coordinates of the first point:
#Input three number coordinates separated by commas: 3,5,4
#Enter 3 coordinates of the second point:
#Input three number coordinates separated by commas: 1,1,1
#The distance between point (3.0, 5.0, 4.0) and (1.0, 1.0, 1.0) is: 5.39

#Process finished with exit code 0
