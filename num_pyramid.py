rw = int(input('Enter number of rows: '))
i = 1
j = 1
while i <= rw:                    #print rows
    j = 1
    while j <= i:
        temp = i * j                  #printing the elements in each row
        print(temp, '\t', end="")
        j += 1
    print('\r')
    i += 1

