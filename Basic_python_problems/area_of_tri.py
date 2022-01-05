"""
area of triangle 
area of triangle using Heron's formula
where s = (a+b+c)/2  semi-perimeter of the triangle formula
area = (s*(s-a)*(s-b)*(s-c)**0.5
why i taken 0.5 we can convert sqrt into power 0.5 
"""

# declaring variables 
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third  number: "))

# semi_perimeter of the triangle 
s = (a+b+c)/2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("the area of the triangle",area)

# if you want area of traingle in int
# print("the area of the triangle",int(area))


