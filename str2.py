print("Enter first string: ")
str1=str(input())
print("Enter second string: ")
str2=str(input())
print("Combined string:")
def chars_mix_up(a, b):
  new_str1 = str2[:1] + str1[1:]
  new_str2 = str1[:1] + str2[1:]

  return new_str1 + ' ' + new_str2
print(chars_mix_up('str1', 'str2'))