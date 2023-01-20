n=int(input("Enter a limit:"))
n1=0
n2=1
n3=n1+n2
count=1
print("fibonacci series: ")
while(count<=n):
    print(n1)
    n1=n2
    n2=n3
    n3=n1+n2
    count+=1

