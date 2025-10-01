# Access Specifiers 
# public, protected, and private members in Python.

class Demo:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

    # Public method
    def public_method(self):
        print("Public Method:", self.public_var)

    # Protected method
    def _protected_method(self):
        print("Protected Method:", self._protected_var)

    # Private method
    def __private_method(self):
        print("Private Method:", self.__private_var)

    # Access private method inside class
    def access_private(self):
        self.__private_method()


if __name__ == "__main__":
    obj = Demo()

    # Public
    print(obj.public_var)      #  allowed
    obj.public_method()        #  allowed

    # Protected
    print(obj._protected_var)  #  allowed, but not recommended
    obj._protected_method()    #  allowed, but considered internal use

    # Private
    # print(obj.__private_var)  #  Error
    obj.access_private()        #  correct way

    # Access private using name mangling (not recommended)
    print(obj._Demo__private_var)  

