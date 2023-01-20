nr = int(input("Enter the number of rows: "))
j = 1
while j <= nr:
    #rows 1 to nr
    i=nr
    #reverse while loop
    while i >= j:
        print("* ",end="")
        i -= 1
    print("\r")
    j += 1