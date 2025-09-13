#local and global variable
x=10  # global variable
def my_function():
    x=4
    y=5 # local variable defined just in the body of this function
    print(x)
    print(y)
my_function()
print(x)

# globle function

x=10 # global variable
def myfunction():
    global x # now it is global variable
    x=8
    y=9
    print(x, y)
myfunction()
print(x) # output "8" not "10".
#print(y) # it will generate an error.
