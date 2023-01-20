def add(m,n):
    return m+n
def subtract(m,n):
    return m-n
def multiply(m,n):
    return m*n
def division(m,n):
    return m/n

print("please select an operation")
print("1.Add","\n2.Substract","\n3.Multiply","\n4.Division")

while True:
    choice = input("Enter your choice :")
    if choice in('1','2','3','4'):
        n1=float(input("Enter the first number :"))
        n2 = float(input("Enter the second number :"))

        if choice == '1' :
            print(n1,"+",n2,"=",add(n1,n2))
        elif choice == '2':
            print(n1,"-",n2,"=",subtract(n1,n2))
        elif choice == '3':
            print(n1,"*",n2,"=",multiply(n1,n2))
        elif choice == '4':
            print(n1, "/", n2, "=", division(n1, n2))
        nxt_calc=input("do you want another calculation? (yes/no) :")
        if nxt_calc == "no":
            break

        else:
            print("invalid request!!")


