str1 = str(input('Enter a string:\n '))
char = str1[0]
char1 = str1[0].lower()                   #storing the first letter ina variable
str1 = str1.replace(char1, '$')    #replacing the first char and its occurences with $
str1 = char + str1[1:]            #printing the first char concatenated with 2nd letter from st1
print('String after  replacing the occurence of first character: \n', str1)