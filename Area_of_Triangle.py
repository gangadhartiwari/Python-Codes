# Area of Triangle - for this we need base and height of triangle 

# 1. If base and height are known:

# base = int(input("Enter the base :- "))
# height = int(input("Enter the height :- "))

# AoT = 0.5*base*height

# print("Area of Triangle is :", AoT)

# --------------------------------------------------------------------------

#2. If all three sides are known (Heron’s formula):

a = int(input())
b = int(input())
c = int(input())

s = (a+b+c)/2

Area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Triangle is :", Area)