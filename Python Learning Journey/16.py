# for loop 
name="Smavia Amir"
print(name)
for i in name:
    print(i)
    
# for loop on indexes
colors=["red","blue","pink","orange","yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
        if(i=="e"):
            print("This is special.")
            
# ranges in python
for i in range(10):
    print(i)
for i in range(5):
    print(i+1)
for k in range(2,15,3):
    print(k)
