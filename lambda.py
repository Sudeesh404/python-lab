a = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
area = lambda a,b: a*b
print("Area of the rectangle: ", area(a,b), "sq.units")
print()
a = int(input("Enter the height of the triangle: "))
b = int(input("Enter the breadth of the triangle: "))
area = lambda a,b: 1/2*a*b
print("Area of the rectangle: ", area(a,b), "sq.units")
print()
a = int(input("Enter the radius of the circle: "))
area = lambda a: 3.14*a**2
print("Area of the circle: ", area(a), "sq.units")
print()
a = int(input("Enter the length of the square: "))
area = lambda a: a**2
print("Area of the square: ", area(a), "sq.units")