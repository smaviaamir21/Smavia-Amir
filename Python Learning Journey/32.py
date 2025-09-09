#for loop with else
for i in range(5):
    print(i)
else:
    print("Now in body of else")


#break
for i in range(9):
    print(i)
    if i==6:
        break   
else:
    print("Now in body of else")

#while loop with else
i=0
while i<7:
    print(i)
    i=i+1
else:
    print("out from while loop")
# break
i=0
while i<7:
    print(i)
    i=i+1
    if i==3:
        break
else:
    print("out from while loop")
