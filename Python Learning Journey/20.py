# break statement
for i in range (11):
    if(i==5):
        print("break the loop here")
        break
    print("5X",i,"=",5*i)

# continue statement
for i in range (11):
    if(i==5):
        print("skip the iteration here")
        continue
    print("5X",i,"=",5*i)

# it will works like do while loop of C++
i=0
while True:
    print(i)
    i=i+1
    if(i%14==0):
        break
