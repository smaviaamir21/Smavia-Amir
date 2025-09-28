# inheritance in python
# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class
class Student(Person):
    def __init__(self, name, age, student_id):
        # call parent constructor
        super().__init__(name, age)
        self.student_id = student_id
    
    def display(self):
        # overriding parent display
        print(f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

# Child class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display(self):
        print(f"Teacher Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

# Example usage
s = Student("Ali", 20, "S123")
t = Teacher("Sara", 35, "Mathematics")

s.display()
t.display()
