a = int(input("Enter upper limit: "))
b = int(input("Enter lower limit: "))
lists = []
for i in range(b,a+1):
    for i in range(1,i):
        if i * i == i:
            string =str[i]
            if int(string[0])%2==0 and (string[1])%2==0 and (string[2])%2==0 and (string[3])%2==0):
                list.append(string)
    print(lists)