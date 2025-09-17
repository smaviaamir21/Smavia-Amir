# lambda function

double=lambda x: x*5
cube=lambda x: x*x*x
avg=lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(3))
print(avg(3,5,10))

# pass lambda function as an argument in function

def appl(fx, value):
    return 6 + fx(value)

print(appl(lambda x: x*x*x, 2))
