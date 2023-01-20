
print("\nChoices:\n1.Addition\n2.subtraction\n3.Division\n4.Multiplication\n5.Exit")  #choices for the operation
while True:
    ch = int(input("\nPlease enter a choice:"))
    if ch in (1, 2, 3, 4):
        a = float(input("\nEnter the first number: "))
        b = float(input("\nEnter the second number: "))


        if ch == 1:
            print("\n", a, " +", b, "=", a+b)
        elif ch == 2:
            print("\n", a, " -", b, "=", a - b)
        elif ch == 3:
            print("\n", a, " / ", b, " = ", a/b)
        elif ch == 4:
            print("\n", a, "*", b, "=", a*b)

    elif ch == 5:
        print("You have exited!!")
        break
    else:
        print("\t\ninvalid choice!! \nPlease enter a valid choice :)")







