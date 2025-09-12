# enumerate function in python
fruits = ['apple','banana','mango']
for index, fruit in enumerate(fruits):
    print(index,fruit)

marks=[12,34,52,36,73,23,1,90,5]
for index,mark in enumerate(marks, start=1):
    print(index,mark)
    if index == 8:
        print("This is the top.")

s='hello'
for index,c in enumerate(s):
    print(index,c)
