str1 = str(input('Enter a string: '))
count = 0

#count each character iin string

for i in range(0,len(str1)):
    if(str1[i] != ' '):               #to exclude the spaces
        count = count + 1

#to display number of char

print("Total no of characters in the given string:", count)
