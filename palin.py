num=int(input("Enter a number:"))
rev=num
sum = 0
while(num!=0):
    r=num%10
    sum=sum*10+r
    num=num//10
if(rev==sum):
    print("The number", rev, "is a palindrome!")
else:
    print("The number",rev, "is not palindrome!")

