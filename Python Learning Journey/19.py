# task 2 for practice

# method 1 with the help of user-input
h=int(input("Enter the hour: "))
if(5<=h<11):
    print("Good Morning!")
elif(11<=h<14):
     print("Good Afternoon!")
elif(14<=h<18):
    print("Good Evening!")
elif(18<=h<24):
    print("Good Night!")            
else:            
    print("You have to sleep now!") 

# method 2 by using time module
import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
h=int(time.strftime('%H'))
m=int(time.strftime('%M'))
s=int(time.strftime('%S'))
if(5<=h<11):
    print("Good Morning!")
elif(11<=h<14):
     print("Good Afternoon!")
elif(14<=h<18):
    print("Good Evening!")
elif(18<=h<24):
    print("Good Night!")            
else:            
    print("You have to sleep now!") 
