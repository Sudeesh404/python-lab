
r = int(input("Enter number of rows: "))

k = 0

for i in range(1, r+1):
    #The outermost loop from i = 1 toi = row + 1

    for space in range(1, (r - i) + 1): #loop to print required sace for each row
        print(end="  ")

    while k!= (2 * i - 1):
        #the while loop prints the required number stars
        print("* ", end="")
        k += 1

    k=0
    print()