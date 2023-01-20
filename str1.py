
print("Enter a word:")
string = input()
print("Word after swapping first and last character:")

mid = string[1:-1]
end = string[-1:]
beg = string[0]
print (end + mid + beg)