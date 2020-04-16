import math

print("Area of triangle")
a = int(input("Enter length of side a"))
b = int(input("Enter length of side b"))
c = int(input("Enter length of side c"))

s = (a+b+c)/2
print(s)
area = math.sqrt( s*(s-a)*(s-b)*(s-c) )
print("Area of triangle is",area)
