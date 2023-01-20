str1 = str(input('\nEnter a string:'))
l = len(str1)
if str1[-3:] == 'ing':
    str1 += 'ly'
else:
    str1 += 'ing'
print('\nNew string =', str1)

