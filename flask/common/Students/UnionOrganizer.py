from .Student import Student
from dataclasses import dataclass

@dataclass
class UnionOrganizer(Student):
    salary: float = 0
    
    def __post_init__(self):
        self.studenttype = 3

    def Input(self, io):
        super().Input(io)
        self.salary = float(io.Input("additionalInput"))

    def Output(self, io):
        return io.Output(student=self)

    
    def toString(self):
        return f"Info about student\nUnionStudent\nID: {self.id}\nName: {self.name}\nAge: {self.age}\nGroup: {self.groupnumber}\nFaculty: {self.faculty}\nSalary:{self.salary}"