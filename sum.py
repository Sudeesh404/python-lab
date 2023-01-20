num = int(input("Enter a number :"))
temp = num                                   #storing the value of num in temp
sm = 0                                      #intial value of num is 0
while(num!=0):
    r = num % 10                        #gets the last digit of num(remainder)
    sm = sm + r                         #addiing sum with the remainder
    num = num // 10                     #excludes the last digit in previous iteration
print("sum of digits in", temp, " = ", sm)

