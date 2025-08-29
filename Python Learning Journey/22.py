#function arguments
def name(fname,mname, lname):
    print("Hello",fname,mname, lname)
name("smavia", "Amir", "Ali")

# required arguments
def average(a,b):
    print("The average is:",(a+b)/2)

a=2
b=3   
average(a, b)

# default arguments
def average(a=3, b=9):
    print("The average is:",(a+b)/2)
average()

# keyword arguments
def average(a=3, b=9):
    print("The average is:",(a+b)/2)
average(b=15, a=9)

