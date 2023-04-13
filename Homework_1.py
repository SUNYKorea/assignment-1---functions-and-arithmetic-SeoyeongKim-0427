# Name: Seoyeong Kim
# SBUID: 115933295
##################### SCORE ######################
####### Score:  2/10  - attemped to write some functions
#################################################
# your output -- All wrong
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/SeoyeongKim-0427/Homework_1.py"
# The temperature is  10  degrees Celsius.
# You should wear a ...did not think of this case. 

# The area of the triangle is : 2.5 , its perimeter is : 27.4402
# The area of the polygon is : 310.0188
# Remove the ellipses (...) when writing your solutions.
import math
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit):

    try:
        float(fahrenheit)

    except ValueError:
        print("Invalid input; the temperature is now 40 which is 4.4 degrees Celsius.")
        return (5/9)*(40 - 32)

    else:
        return int((5/9)*(float(fahrenheit) - 32))

def what_to_wear(celsius):
   clothes = ['puffy jacket', 'scarf', 'sweater', 'light jacket', 'T-shirt', '...did not think of this case.']

   if(celsius < -10):
       wear_this_clothe = clothes[0]
    
   elif(-10 < celsius < 0):
       wear_this_clothe = clothes[1]
    
   elif(0 < celsius < 10):
       wear_this_clothe = clothes[2]
       
   elif(10 < celsius < 20):
       wear_this_clothe = clothes[3]
       
   elif(celsius > 20):
       wear_this_clothe = clothes[4]
    
   else:
       wear_this_clothe = clothes[5]
       #The purpose of this code is for Celsius degrees exactly at 10, 20, etc.
       #because the clothes for such degrees are not defined.
    
   print("The temperature is ", celsius, " degrees Celsius.")
   print("You should wear a", wear_this_clothe, "\n")
       
       

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(1/2 * ( ((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((x1 * y3) + (x2 * y1) + (x3 * y2)) ))

def euclidean_distance(x1, y1, x2, y2):
    return ( ((x1 - x2) ** 2) + ((y1 - y2) ** 2) ) ** 0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x2, y2, x3, y3)
    s3 = euclidean_distance(x3, y3, x1, y1)
    return round(s1 + s2 + s3, 4) #The perimeter is rounded because it could be too long


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    return deg*(math.pi/180)

def apothem(number_sides, length_side):
    return length_side / 2*math.tan(180/number_sides)

def polygon_area(number_sides, length_side):
   return round(number_sides * length_side * apothem(number_sides, length_side), 4)
    #The area is rounded because it could be too long


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 50
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, x2, x3, y1, y2, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

