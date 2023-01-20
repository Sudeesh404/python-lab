clr_lst = ["orange", "purple", "red", "blue","green", ]

clr_lst2 = ["violet", "red", "orange", "yellow"]
print("\ncolor list 1 =", clr_lst)
print("color list 2 =", clr_lst2)
x = set(clr_lst)
y = set(clr_lst2)
z = x.difference(y)
print("\n colors from color list 1 not contained in color list 2 is : ", z)
