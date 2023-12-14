class Employee:
    id:int
    name:str
    department:str
    salary:int

    def set_emp(self,id,name,dept,sal):
        self.id=id
        self.name=name
        self.department=dept
        self.salary=sal

    def display_emp(self):
        print(self.id,self.name,self.department,self.salary)

#create an object
emp1=Employee()
emp1.set_emp(123,"Ram","HR",50000)

emp2=Employee()
emp2.set_emp(345,"Vijay","QA",45000)

#print
emp1.display_emp()
emp2.display_emp()