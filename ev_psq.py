# import math
print('\nFour digit perfect square numbers with all digits even:\n')
r1 = int(input("Please enter starting number :"))
r2 = int(input("\nPlease enter ending number :"))
temp1 = r1
temp2 = r2
e_count = 0
if( r1 >= 1000 and r2 <= 9999):
    for i in range(r1,r2,1):
        while r1 > 0:
            rem = r1 % 10
            if rem % 2 == 0:
                e_count+=1
            r1 = r1 / 10
            if e_count == 4:
                print('r1')
#     while r1 <= r2:
#         r = math.sqrt(r1)
#         if r * r == r1:
#             print('Perfect square in between', temp1, 'and', temp2, 'is', r1)
#         r1+=1
# else:
    #print("Enter a range in between 1000 and 9999!!!")