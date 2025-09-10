#exception handling in python
try:
    # taking input from user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # check division
    result = a / b
    print("Result:", result)

# handle division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

# handle invalid input (like entering text instead of number)
except ValueError:
    print("Error: Please enter only numbers!")

# handle any other unknown error
except Exception as e:
    print("Unexpected Error:", e)

#runs always whether there is an error or not
finally:
    print("Program ended safely.")

# raising custom error

a=int(input("Enter a value between 4 and 9: "))
if(a<4 or a>9):
    raise ValueError("value must be between 4 and 9.")
