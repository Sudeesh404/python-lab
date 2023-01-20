list1 = [1, 2, 3, 66, 77, 88, 8, 3, 5, 6, 4, 10, 11]
new = [i for i in list1 if i % 2 != 0]
print('\nOriginal list: ',"\n", list1)
print('\nList after removing the even numbers:',"\n", new)