num=int(input("Enter a three digit number:"))
sum=0
temp=num
while(num!=0):
    r=num%10
    sum=r*r*r+sum
    num=num//10
if(sum==temp):
    print("number is amstrong!")
else:
    print("number is not amstrong")