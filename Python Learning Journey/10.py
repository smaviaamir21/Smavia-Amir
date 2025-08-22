# Strings Slicing and Operations on Strings in Python

fruit="Apple"
fruit_length=len(fruit)
print(fruit_length)# show lenth of string

print(fruit[0:5]) # including 0 but excluding 5

print(fruit[:3])  
"""automatically consider 0 if 
we skip the starting index"""
print(fruit[:])

# negative slicing
print(fruit[-4:-1]) # fruit[1:4]
print(fruit[:len(fruit)-3]) #fruit[0:2]
