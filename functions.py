'''
1    Write a function called calculate_area that takes base and
height as an input and returns and area of a triangle.
Equation of an area of a triangle is,
area = (1/2)*base*height

2    Modify above function to take third parameter shape type.
It can be either "triangle" or "rectangle".
Based on shape type it will calculate area.
Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape

3    Write a function called print_pattern that takes integer
as an argument and prints following pattern if input number is 3,
*
**
***

if input is 4 then it should print
*
**
***
****
Basically number of lines it prints is equal to that number.
(Hint: you need to use two for loops)
'''

def area_triangle(base, height):
    ''' calculates area of triangle '''
    return 0.5 * base * height

def area_shape(length1, length2, shape = "triangle"):
    ''' calculates area of triangle or rectangle'''
    if shape == "rectangle":
        return length1 * length2
    return 0.5 * length1 * length2

def print_pattern(n):
    ''' print triangle pattern '''
    for k in range(1, n+1):
        #print("k=", k)
        for _ in range(k):
            #print("l=", l)
            print("*", end="")
        print("", end='\n')

def driver():
    ''' driver function '''
    print("Area of triangle:", area_triangle(2, 2))
    print("Are of shape:", area_shape(2, 2, "rectangle"))
    print_pattern(6)

driver()
