#nested if
num=int(input("Enter a number: "))
if(num<0):
    print("Number is Negative.")
elif(num>0):
    if(num<=10):
        print("In between 0_10")   
    elif(num<=20):     
        print("In between 10_20")
    elif(num<=30):
        print("In between 20_30")
    else:
        print("Greater than 30")
else:
    print("Equal to 0.")
