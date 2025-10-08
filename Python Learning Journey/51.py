class Employee:
    # CLASS VARIABLE: shared by ALL objects of the class
    # If you change it using the class name, it affects all objects.
    companyName = "Apple"

    def __init__(self, name):
        # INSTANCE VARIABLES: unique for EACH object
        # Each employee will have their own 'name' and 'raise_amount'
        self.name = name
        self.raise_amount = 0.02

    def showDetails(self):
        # Accessing both instance and class variables
        print(f"The name of the Employee is {self.name} "
              f"and the raise amount in {self.companyName} is {self.raise_amount}")


# Creating first object (emp1)
emp1 = Employee('Smavia')
emp1.raise_amount = 0.3            # Changing instance variable (specific to emp1)
emp1.companyName = "Apple Pakistan"  # Changing class variable only for emp1 (instance-level)
emp1.showDetails()                 # Uses emp1's own companyName and raise_amount


# Changing CLASS VARIABLE for the entire class
Employee.companyName = "Google"    # Affects all future objects (and any that didn’t override it)
print(Employee.companyName)        # Shows updated class variable value


# Creating second object (emp2)
emp2 = Employee('Aqba')
emp2.raise_amount = 0.5            # Instance variable for emp2
emp2.showDetails()                 # Uses class variable (Google) and emp2's raise_amount
