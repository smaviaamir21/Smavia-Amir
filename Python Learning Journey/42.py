# map
l=[1,4,5,2,7,2,1,8]
newl= list(map(lambda x: x*x*x,l))
print(newl)

# filter
def filter_function(a):
    return a>2

newl=list(filter(filter_function,l))
print(newl)

# reduce
from functools import reduce
numbers=[1,2,3,4,5,6,7]
sum=reduce(lambda x,y: x + y ,numbers)
print(sum)
