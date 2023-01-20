km=float(input("Enter the value in kilometers:"))
mil_conv=0.62137 # 1km = 0.62137 miles, so we can get equivalent miles by multiplying km with mil_conv value
miles=km*mil_conv
print("%f kilometers is equal to %f miles" %(km,miles))