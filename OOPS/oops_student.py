class Student:
    roll_no:int
    name:str
    course:str

    def set_stud(self,rollno,name,course):
        self.roll_no=rollno
        self.name=name
        self.course=course
    
    def display_stud(self):
        print(self.roll_no,self.name,self.course)

stud1=Student()
stud1.set_stud(11,"Souparna","CSE")

stud2=Student()
stud2.set_stud(12,"Najiya","CSE")

stud3=Student()
stud3.set_stud(13,"Sree lakshmi","CSE")

stud1.display_stud()
stud2.display_stud()
stud3.display_stud()