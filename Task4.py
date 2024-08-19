import math

radius = float(input("enter the radius"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 3)
print("Area of the circle is :", area)

print(f"Area of the circle is : {area: .3f}")