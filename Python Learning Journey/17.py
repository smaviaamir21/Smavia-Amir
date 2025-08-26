# while loop
i=0
while(i<=5):
    print(i)
    i=i+1
# while loop , taking user input
k=int(input("Enter a positive number:"))
while(k<=0):
    k=int(input("Enter again,\n it must be a positive number:"))  # in the body of loop
print(k, ": this K was required.")    # out from while loop body
