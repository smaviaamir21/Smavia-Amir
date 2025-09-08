#methods of 

s1={1,2,5,7,8,12,13}
s2={3,4,6,9,12,13}
print(s1,s2)
s1.update(s2) # adds the elements of s2 in s1
print(s1)

#union in sets

s1={1,2,5,7,8,12,13}
s2={3,4,6,9,12,13}
print(s1.union(s2))

# intersection in sets
s1={1,2,5,7,8,12,13}
s2={3,4,6,9,12,13}
print(s1.intersection(s2))


# symmetric difference

s1={1,2,3,4,5,6}
s2={1,2,3,4}
print(s1.symmetric_difference(s2))

# difference and difference_updates

s1={1,2,5,7,8,12,13}
s2={3,4,6,9,12,13}
print(s1.difference(s2))


# build in methods

s1={1,2,5,7,8}
s2={3,4,6,9}
print(s1.isdisjoint(s2))  # check is there is nothing common b/w two sets

s1={1,2,5,7,86,7, 3,4}
s2={5,7,3}
print(s1.issuperset(s2))   # check wheather all the elements of s2 is in s1
print(s2.issubset(s1))   # check if all the elements of original set (s2) present in perticuler set (s1)

s1={1,2,5,7,86,7, 3,4}
s1.add(56)   # add any element
print(s1)
#remove()/discard()
s1.remove(2)
print(s1)    # remove the perticuler item from the set

s1.discard(234)   # it will not generate an error if the perticuler item is not in set
print(s1)  

#pop()
v={23,"table", "chair", "pen"}
item=v.pop()
print(v)
print(item)


# del v
# print(v)   # it will generate error because v is deleted

v.clear()
print(v)  # it will remove all the items from the set and show "set()" only

info={"Smavia","Girl", 19}
if "Girl" in info:
    print("Girl string is present in set")
else:
     print("Girl string is not present in set")

