# constructor in python
class person:
    def __init__(self,name,age,level):
        print("Hye i am a coder!")
        self.name=name
        self.age=age
        self.level=level
    def info(self):
        print("{self.name} is {self.age} years old and in {self.level} class.")


a=person('Smavia',12,8)
b=person('Noor',10,7)
c=person('Aqba',10,7)
a.info()
b.info()
c.info()
