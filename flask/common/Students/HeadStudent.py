from .Student import Student
from dataclasses import dataclass

@dataclass
class HeadStudent(Student):
    phone: int = "0"
    
    def __post_init__(self):
        self.studenttype = 2

    def Input(self, io):
        super().Input(io)
        self.phone = io.Input("additionalInput")

    def Output(self, io):
        return io.Output(student=self)
    
 
    def toString(self):
        return f"Info about student\nHeadStudent\nID: {self.id}\nName: {self.name}\nAge: {self.age}\nGroup: {self.group}\nFaculty: {self.faculty}\nPhone:{self.phone}"