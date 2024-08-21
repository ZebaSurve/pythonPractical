side1 = int(input("Enter the first side"))
side2 = int(input("Enter the second side"))
side3 = int(input("Enter the third side"))

if side1 == side2 == side3:
    print("the triangle is equilateral triangle")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("the triangle is an isosceles triangle")

else:
    print("the triangle is scalene triangle")