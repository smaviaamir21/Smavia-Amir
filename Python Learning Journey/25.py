# f-string
letter="Hey my name is {0} and I am from {1}"
name="Smavia"
city="Lahore"
print(letter.format(name,city))
print(f"Hey my name is {name} and I am from {city}")          
print(type(letter.format(name,city)))   # string type
print(f"Hey my name is {{name}} and I am from {{city}}")  # show the string as it is {name} and {city}        

price=49.03499
txt=f"for only {price:.2f} dollars!"   # print two digits after decimal
print(txt) 
print(txt.format())

print(f"{2*44}")
print(type(f"{2*44}"))

# docstrings in python
def square(n):
    '''Takes in a number n and, returns the square of n'''
    print(n**2)
n=int(input("Enter a number: "))
square(n)
print(square.__doc__)
