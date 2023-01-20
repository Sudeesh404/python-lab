# (a) printing +ve numbers in a list using list comprehnsion
# list1 = [1, -1, 5, 7, -5, -3, 2, -6, -7, -8, 5, -88, 32, 9]
# list2 = [ x for x in list1 if x >= 0]
# print('\nOriginal list:', list1)
# print('\nList of positive numbers from list1:', list2)

#(b) printing square of n numbers
# list3 = [1, 2, 3, 4, 5, 6, 9, 10, 16]
# sq = [x*x for x in list3]
# print('\nOriginal list:', list3)
# print('\nList of square of numbers :', sq)



#(c) printing vowels from a word
def vowel(text):
    vowels = 'aeiouAEIOU'
    print("\nVowels in the word are: ")
    print([i for i in text if i in vowels])
wrd=str(input("Enter a word: "))
vowel(wrd)

#list of ordinal values of each element of a word

