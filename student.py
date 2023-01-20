print("Please enter your name:")
nm=str(input())
english = float(input("Please enter English Marks: "))
mathematics = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))

total = english + mathematics + computers + physics + chemistry
percentage = (total / 500) * 100
print("\nMr",nm,"here is your results:")
print("\nTotal Marks = %f" % total)
print("Marks Percentage = %f" %percentage)
