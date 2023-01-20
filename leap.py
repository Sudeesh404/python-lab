y1 = int(input("\nEnter the current year: "))
y2 = int(input("\nEnter the final year: "))
print( "\nList of leap years from", y1, "to", y2,'are:')
i = y1
while i <= y2:
    if i % 4 == 0:
        print(i)
    i += 1

