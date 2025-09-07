# recursive function 

# finding factorial of a number
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter a number:"))
# f=factorial(num)
# print(f)
print(factorial(num))

# print fibonacci sequance
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
num=int(input("Enter a number: "))
for i in range(num):
    print(fibonacci(i))

