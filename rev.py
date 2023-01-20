num = int(input("Enter a number: "))
rev = num
sm = 0
while num != 0:
    r = num % 10
    sm = sm * 10 + r
    num = num // 10
print( "The reverse of number", rev, "is", sm)
