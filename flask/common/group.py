from flask import render_template, jsonify
from flask import request

from common.StorageStrategies import MongoStorage

from .Students.HeadStudent import HeadStudent
from .Students.Student import Student
from .Students.UnionOrganizer import UnionOrganizer



templatePath: str = ''

class Group:
    path =  ''
    def __init__(self,storage,io):
        self.storage = storage
        self.io = io

    def ShowForm(self, id):
        return self.storage.GetStudent(id).Output(self.io)

    def ShowGroup(self):
        return render_template('group.tpl', items=self.storage.GetStudents())

    def Add(self):
        if isinstance(self.storage, MongoStorage):
            student = self.storage.GetStudent(self.io.Input('id'))
        else:
            student = self.storage.GetStudent(int(self.io.Input('id')))
        
        studentType = request.form.get('studentTypeSelect')
       
        if studentType == 'studentTypeOption_head':
            student = HeadStudent()
        elif studentType == 'studentTypeOption_organizer':
            student = UnionOrganizer()
        elif studentType == 'studentTypeOption_base':
            student = Student()
            
        student.Input(self.io)
        
        self.storage.Add(student)
        
        return self.ShowGroup()

    def Delete(self, id):
        self.storage.Delete(id)
        return self.ShowGroup()

    def APIGroup(self):
        ids = []
        for student in self.storage.GetStudents():
            ids.append([student.id, student.name])
        return jsonify({'ids': ids})

    def APIAdd(self):
        print('**********************')
        print(request.json)

        studentType = int(request.json.get("studentType", 0))
        student = Student()
        if studentType == 2:
            student = HeadStudent()
        elif studentType == 3:
            student = UnionOrganizer()

        student.Input(self.restio)
        self.storage.Add(student)
        return ''

    def APIGet(self, id):
        student = self.storage.GetStudent(id)
        print(student.__dict__)
        return jsonify(student.__dict__)

    def APISet(self, id):
        student = self.storage.GetStudent(id)

        isTypeReceived = request.json.get("studentType") is not None
        if isTypeReceived:
            studentType = int(request.json.get("studentType"))
            if studentType == 1 and isinstance(student, Student) is False:
                student = Student()
            elif studentType == 2 and isinstance(student, HeadStudent) is False:
                student = HeadStudent()
            elif studentType == 3 and isinstance(student, UnionOrganizer) is False:
                student = UnionOrganizer()

        student.Input(self.restio)
        self.storage.Add(student)
        return ''

    def APIDelete(self, id):
        self.storage.Delete(id)
        return ''
