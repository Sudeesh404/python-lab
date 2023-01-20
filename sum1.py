list1 = []#8, 7, 11, 12, 41, 14]
n = int(input("Enter number of items:"))
for i in range(n):
    x = int(input("Enter item: "))
    list1.append(x)
print("The List = ", list1)
i = 0
sum = 0
while i < len(list1):
    sum = sum + list1[i]
    i +=1
print("\nSum of the ",n, "items in the list: ", sum)
