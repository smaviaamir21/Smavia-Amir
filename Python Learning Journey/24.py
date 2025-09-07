# tuple in python
tup=(1,2,3,78,3521, 23)
# tup[0]=90    it will generate an error because we could not change the tuple.
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[4])
print(tup[-3])

if 78 in tup:
     print("yes 78 is in this tuple.")

# to show the tuple from one index to other,  we have touse this method:
tup2=tup[0:4]
print(tup2)
tuple1=(0,1,2,31,4,5,6,7,5,3,6,4,5)
print(len(tuple1))
res=tuple1.count(3) # count how many numbers of times "3" is in the index
print(res)
res=tuple1.index(3) # find the index where is "3"
print(res)
res=tuple1.index(6,4,12) # find the index between 4 and 12 where is "6"
print(res)

# tuple methods

countries=("Pakistan", "Afghanistan", "Bangladesh", "Shrilanka")
countries1=("Vietnam","India","China")
SouthEastAsia=countries+countries1
print(SouthEastAsia)

#change the tuple into list
temp=list(countries)
temp.append("China")  # add item
temp.pop(3)  #remove item
temp[2]="Finland"  # change item
#change that list into tuple
countries=tuple(temp)
print(countries) #this is the way through which we can indirectly change the tuple.

