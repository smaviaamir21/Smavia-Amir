# decorators in python
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning!")
        fx(*args,**kwargs)
        print("Thanks for using this function.")
    return mfx

@greet
def hello():
    print("Hello World!")
def add(a,b):
    print(a+b)

hello()
greet(add)(2,3)   # another method 

import logging
def log_function_call(func):
    def decorated(*args,**kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result= func(*args,**kwargs)
        logging.info(f"{func.__name__}returned {result}")
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b
a=3
b=4
my_function(a,b)
