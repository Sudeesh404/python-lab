#7
list1 = []
list2 = []
print("\nEnter the integer values for first list : ")
while True:
    x = int(input("\nValue: "))
    list1.append(x)
    choice = str(input("\nwant to quit!!? enter yes: "))
    if choice == "yes":
        print('\nValues inserted successfully into list 1.')
        break


print("\nEnter the integer values for second list : ")
while True:
    y = int(input("\nValue: "))
    list2.append(y)
    choice = str(input("\nwant to quit!!? enter yes: "))
    if choice == "yes":
        print('\nValues inserted successfully into list 2.')
        break
print("\nList 1 = ", list1)
print("\nList 2 =", list2)

p = len(list1)
q = len(list2)
if p == q:
    print("\nList 1 and List 2 are of same length")
else:
    print("\nList 1 and List 2 are of different length")

sum1 = 0
for i in range(0,p):
     sum1 = sum1 + list1[i]
print("\nSum of numbers in list 1 =", sum1)

sum2=0
for j in range(0,q):
    sum2 = sum2 + list2[j]
print("\nSum of numbers in list 1 =", sum2)
if sum1 == sum2:
    print('\nThe lists sums to same value,.')
else:
    print('\n Lists sums to different value.')

r = set(list1)
s = set(list2)
t = r.intersection(s)
print("\nValues occur in both list are :", list(t))





