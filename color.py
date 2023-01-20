color_lst = []

# no of elements
n = int(input("Enter number of elements : "))

print("Enter name of colors:")
# getting elemts from usr
for i in range(0, n):
    ele =(input())

    color_lst.append(ele)  # adding the element at end of list
print("color list=",color_lst)
print( "first and last color = [%s , %s]"%(color_lst[0],color_lst[-1]))
