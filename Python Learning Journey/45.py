# classes and objects

class person:
    name =  "Smavia Amir"
    occupation = "Software Engineer"
    university = "UOL"
    semester = "3rd"
    # function in class
    def info(self):
        print(f"{self.name} a {self.occupation} studing in {self.university} in {self.semester}")
a=person()
print(a.name)
print("My name is", a.name,". My occupation is ", a.occupation
      ,". I am from university ", a.university,"and i am currently in ", a.semester, "semester. ")

a.info()  # function call

#change any object from class in this way 
a.name="Noor"
print(a.name)  # output must be 'Noor' but just here.
