#to count occurrences of each word in a line of text

str1 = str(input('Enter string: '))
str2 = str1.split()
k = {}
for j in str2:
    if j in k:
        k[j] +=1
    else:
        k[j] = 1
print('Occurence of each word in the string :', k)



