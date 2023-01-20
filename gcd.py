cd = []
dc = []
#declaring two lists for storing the values of divisors
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
if n1 == 0:
    print("Greatest common divisor of", n1,"and", n2, "is", n2) #if any of the input is zero the other number is gcd
elif n2==0:
    print("Greatest common divisor of", n1, "and" , n2, "is", n1)
elif n1!=0 and n2!=0:
    for i in range(1, n1+1):
        if n1 % i == 0:
            cd.append(i)
#storing values of divisors in list cd

    for i in range(1,n2+1):
        if n2 % i == 0:
            dc.append(i)
#storing values of divisors in list dc

print("\nDivisors of", n1, "are: ")
print(cd)
#list of divisors of first num
x = set(cd)
#conversion of list into set
print("\nDivisors of", n2, "are: "),
print(dc)
#list of dividors of second num
y = set(dc)
#list to set
print("\nCommon divisors of", n1,"and", n2, "are: ")
z = x.intersection(y)
#to find the common divisors of the two num
print(z)
print("Greatest common divisor of", n1,"and", n2, "is", max(z),".")
#printing the highest num from list of common divisors






