class Employee:
    Company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.Company}")

    @classmethod
    def chargeCompany(cls, newCompany):
        cls.Company=newCompany


e1 = Employee()
e1.name="Harry"
e1.show()
e1.chargeCompany("Tesla")    #class method
e1.show()
print(Employee.Company)
