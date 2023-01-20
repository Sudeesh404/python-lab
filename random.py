import random
import string
print("Generate a random color:")
print("#{:06x}".format(random.randint(0,0xFFFFFF)))
print("\n Generta e an alphabetical string:")
max_len=255
s=""
for i in range(random.randint(1,max_len)):
   s += random.choice(string.ascii_letters)
   print(s)
print("Generate a random value between 2 integers, inclusive")
print(random.randint(0,10))
print(random.randint(-7,7))
print(random.randint(1,1))
print("Generate random multiple of 7 between 0 and 70:")
print(random.randint(0,10)*7)
print("Generate random multiple of 8 between 0 and 80:")
print(random.randint(0,10)*8)