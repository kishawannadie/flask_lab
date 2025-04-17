from dataclasses import dataclass

@dataclass
class Student:
    id: int = 0
    name: str = ""
    age: int = 0
    groupnumber: str = ""
    faculty: str = ""
    studenttype: int = 1

    def Show(self):
        return "Student Edit"

    def getData(self):
        return self.__dict__

    def Input(self, io):
        self.id = int(io.Input('id'))
        self.age = int(io.Input('age'))
        self.name = io.Input('name')
        self.groupnumber = io.Input('groupnumber')
        self.faculty = io.Input('faculty')

    def Output(self, io):
        return io.Output(self)

    def setData(self, d):
        if d:
            self.__dict__.update(d)